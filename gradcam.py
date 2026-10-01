import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# ==========================
# Load Model
# ==========================
model = tf.keras.models.load_model("dfu_2class_model.keras")

# Class labels
classes = ["Healthy", "Ulcer"]

# ==========================
# Input Image
# ==========================
img_path = input("Enter image path: ")

img = cv2.imread(img_path)

if img is None:
    print("❌ Image not found. Check path.")
    exit()

# Resize + preprocess
img = cv2.resize(img, (224, 224))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

input_img = np.expand_dims(img_rgb / 255.0, axis=0)

# ==========================
# Prediction
# ==========================
preds = model.predict(input_img, verbose=0)[0]
class_idx = np.argmax(preds)

print("\n==========================")
print("Prediction:", classes[class_idx])
print("Confidence:", np.max(preds) * 100)
print("==========================\n")

# ==========================
# Grad-CAM (NO GRADIENT VERSION)
# ==========================

# Get MobileNetV2 base model
base_model = model.layers[0]

# Find last Conv layer safely
last_conv_layer = None
for layer in reversed(base_model.layers):
    if "conv" in layer.name.lower():
        last_conv_layer = layer
        break

if last_conv_layer is None:
    print("❌ No Conv layer found in base model")
    exit()

# Feature extraction model
feature_model = tf.keras.Model(
    inputs=base_model.input,
    outputs=last_conv_layer.output
)

conv_output = feature_model(input_img, training=False)[0].numpy()

# ==========================
# Simple Heatmap (channel average)
# ==========================
heatmap = np.mean(conv_output, axis=-1)

# Normalize safely
heatmap = np.maximum(heatmap, 0)

if np.max(heatmap) != 0:
    heatmap = heatmap / np.max(heatmap)

# Resize heatmap
heatmap = cv2.resize(heatmap, (224, 224))

heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

# Overlay
superimposed = cv2.addWeighted(img, 0.6, heatmap, 0.4, 0)

# ==========================
# Display Results
# ==========================
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Heatmap")
plt.imshow(heatmap)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Grad-CAM Style Output")
plt.imshow(cv2.cvtColor(superimposed, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()