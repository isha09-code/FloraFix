# diagnosis/predictor.py
import tensorflow as tf
import numpy as np
import json
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

# Load model once
MODEL_PATH = os.path.join("ml_models", "plant_disease_final.keras")
CLASS_PATH = os.path.join("ml_models", "class_names.json")

MODEL = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r") as f:
    CLASS_NAMES = json.load(f)

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # match training size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = MODEL.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(preds)]
    confidence = float(np.max(preds) * 100)

    return predicted_class, round(confidence, 2)
