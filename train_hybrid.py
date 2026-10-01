import tensorflow as tf
from tensorflow.keras import layers, Model
import numpy as np
import os

# ==========================
# Dataset Path
# ==========================
dataset_path = r"C:\Users\vemul\OneDrive\Desktop\DFU_Project\dataset"

img_size = (224, 224)
batch_size = 16

# ==========================
# Load Dataset
# ==========================
train_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

class_names = train_ds.class_names
print("Classes:", class_names)

# Normalize
normalization = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization(x), y))
val_ds = val_ds.map(lambda x, y: (normalization(x), y))

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# ==========================
# Input Layer
# ==========================
input_layer = layers.Input(shape=(224, 224, 3))

# ==========================
# EfficientNet Branch
# ==========================
effnet = tf.keras.applications.EfficientNetB0(
    include_top=False,
    weights="imagenet",
    input_tensor=input_layer
)
effnet.trainable = False

x1 = layers.GlobalAveragePooling2D()(effnet.output)

# ==========================
# InceptionResNetV2 Branch
# ==========================
inception = tf.keras.applications.InceptionResNetV2(
    include_top=False,
    weights="imagenet",
    input_tensor=input_layer
)
inception.trainable = False

x2 = layers.GlobalAveragePooling2D()(inception.output)

# ==========================
# Fusion Layer
# ==========================
combined = layers.concatenate([x1, x2])

x = layers.Dense(256, activation="relu")(combined)
x = layers.Dropout(0.3)(x)
x = layers.Dense(128, activation="relu")(x)
x = layers.Dropout(0.3)(x)

output = layers.Dense(2, activation="softmax")(x)

# ==========================
# Model
# ==========================
model = Model(inputs=input_layer, outputs=output)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ==========================
# Train Model
# ==========================
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)

# ==========================
# Save Model
# ==========================
model.save("dfu_hybrid_model.keras")

print("✅ Hybrid Model Training Completed & Saved!")