import os
import numpy as np
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Dense
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# -------------------
# Load ML model & class names once
# -------------------
# Monkey-patch Dense to fix Keras version mismatch (quantization_config)
from tensorflow.keras.layers import Dense
original_dense_init = Dense.__init__

def custom_dense_init(self, *args, **kwargs):
    kwargs.pop('quantization_config', None)
    original_dense_init(self, *args, **kwargs)

Dense.__init__ = custom_dense_init

MODEL_PATH = os.path.join(str(settings.BASE_DIR.parent), "frontend", "plant_disease_sequential_model.keras")
CLASS_NAMES_PATH = os.path.join(settings.BASE_DIR, "ml_models", "class_names.json")

model = load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH, "r") as f:
    CLASS_NAMES = json.load(f)

if isinstance(CLASS_NAMES, dict):
    CLASS_NAMES = list(CLASS_NAMES.values())

# -------------------
# Helper for preprocessing
# -------------------
def preprocess_image(img_path, target_size=(128, 128)):  # ✅ match model input
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# -------------------
# Main View
# -------------------
def index(request):
    result = None
    confidence = None
    uploaded_image_url = None

    if request.method == "POST" and request.FILES.get("plantImage"):
        # Save uploaded image
        image_file = request.FILES["plantImage"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.path(filename)
        uploaded_image_url = fs.url(filename)

        # Predict
        img_array = preprocess_image(uploaded_image_path)
        # Apply softmax since the model's last layer is linear (logits)
        raw_predictions = model.predict(img_array)[0]
        probabilities = tf.nn.softmax(raw_predictions).numpy()
        
        predicted_class = np.argmax(probabilities)
        confidence = round(float(100 * np.max(probabilities)), 2)
        
        # Prevent IndexError if the model has fewer classes than the JSON
        if predicted_class < len(CLASS_NAMES):
            result = CLASS_NAMES[predicted_class]
        else:
            result = f"Unknown Class #{predicted_class}"

    return render(request, "diagnosis/diagnose.html", {
        "result": result,
        # "confidence": confidence,
        "uploaded_image_url": uploaded_image_url,
    })

# -------------------
# API View for Frontend
# -------------------
@csrf_exempt
def predict_api(request):
    # Handle CORS Preflight
    if request.method == "OPTIONS":
        response = JsonResponse({"message": "CORS preflight successful"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    if request.method == "POST" and request.FILES.get("plantImage"):
        try:
            image_file = request.FILES["plantImage"]
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            uploaded_image_path = fs.path(filename)
            uploaded_image_url = request.build_absolute_uri(fs.url(filename))

            img_array = preprocess_image(uploaded_image_path)
            # Apply softmax since the model's last layer is linear (logits)
            raw_predictions = model.predict(img_array)[0]
            probabilities = tf.nn.softmax(raw_predictions).numpy()
            
            predicted_class = np.argmax(probabilities)
            confidence = round(float(100 * np.max(probabilities)), 2)
            
            # Prevent IndexError if the model has fewer classes than the JSON
            if predicted_class < len(CLASS_NAMES):
                result = CLASS_NAMES[predicted_class]
            else:
                result = f"Unknown Class #{predicted_class}"

            response = JsonResponse({
                "success": True,
                "result": result,
                "confidence": confidence,
                "uploaded_image_url": uploaded_image_url
            })
            response["Access-Control-Allow-Origin"] = "*"
            return response
        except Exception as e:
            response = JsonResponse({"success": False, "error": str(e)}, status=500)
            response["Access-Control-Allow-Origin"] = "*"
            return response
    
    response = JsonResponse({"success": False, "error": "Invalid request or missing image"}, status=400)
    response["Access-Control-Allow-Origin"] = "*"
    return response
