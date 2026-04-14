from django.test import TestCase
import tensorflow as tf
import numpy as np
import json
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

# -------------------------------
# CONFIG
# -------------------------------
MODEL_PATH = "ml_models/plant_disease_best.keras"
CLASS_NAMES_PATH = "ml_models/class_names.json"
TEST_IMAGE = "test_images/sample_leaf.jpeg"  # test image path
IMG_SIZE = (128, 128)  # must match training size

# -------------------------------
# 1. Load Model
# -------------------------------
print("🔹 Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

# -------------------------------
# 2. Load Class Names
# -------------------------------
with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)
print(f"✅ Loaded {len(class_names)} classes.")

# -------------------------------
# 3. Load and Preprocess Image
# -------------------------------
if not os.path.exists(TEST_IMAGE):
    raise FileNotFoundError(f"Test image not found at: {TEST_IMAGE}")

print(f"🔹 Processing image: {TEST_IMAGE}")
img = load_img(TEST_IMAGE, target_size=IMG_SIZE)
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# ✅ Correct preprocessing
img_array = preprocess_input(img_array)

# -------------------------------
# 4. Predict
# -------------------------------
print("🔹 Running prediction...")
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=1)[0]
confidence = np.max(predictions)

# -------------------------------
# 5. Output
# -------------------------------
predicted_disease = class_names[str(predicted_class_index)]

print("\n=== Prediction Result ===")
print(f"Predicted Disease: {predicted_disease}")
print(f"Confidence: {confidence * 100:.2f}%")
print("==========================\n")