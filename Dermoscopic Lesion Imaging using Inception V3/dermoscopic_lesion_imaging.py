# -*- coding: utf-8 -*-
"""Dermoscopic lesion imaging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nvrOTPrpU-iFZX6aXCh85uu4dhJgzBfR
"""

!jupyter nbconvert --to html "/content/Dermoscopic_lesion_imaging (1).ipynb"

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

!nvidia-smi

# Load training labels from the CSV file
train_labels = pd.read_excel("/content/KCDH2024_Training_GroundTruth.xlsx")
train_labels['image'] = train_labels['image'].astype(str) + '.jpg'

# Directory paths for training and test images
train_dir = "/content/drive/MyDrive/data science/Ai Ml wncc/KCDH2024_Training_Input_10K"
test_dir = "/content/drive/MyDrive/data science/Ai Ml wncc/KCDH2024_Test_Input"

# Image data generators for training and validation
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_labels,
    directory=r"/content/drive/MyDrive/data science/Ai Ml wncc/KCDH2024_Training_Input_10K",
    x_col="image",
    y_col=train_labels.columns[1:],
    batch_size=32,
    shuffle=True,
    class_mode="raw",
    target_size=(600, 450)
)

# Load InceptionV3 model
base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(600, 450, 3))

# Add custom top layers for classification
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(7, activation='softmax')(x)

# Combine base model and top layers
model = Model(inputs=base_model.input, outputs=predictions)

# Freeze the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=10)

# Define the directory containing the test images
test_directory = '/content/drive/MyDrive/data science/Ai Ml wncc/KCDH2024_Test_Input'

# Get the list of filenames of the test images
test_filenames = os.listdir(test_directory)

# Initialize lists to store predictions and corresponding filenames
predictions = []
image_filenames = []

import os
import numpy as np
from keras.preprocessing import image

for filename in test_filenames:
    try:
        # Load and preprocess the test image
        img = image.load_img(os.path.join(test_directory, filename), target_size=(600, 450))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = img / 255.0  # Rescale pixel values

        # Make prediction on the test image
        prediction = model.predict(img)

        # Append the prediction and corresponding filename to the lists
        predictions.append(prediction)
        image_filenames.append(filename)
    except Exception as e:
        print(f"Error processing file {filename}: {str(e)}")

# Convert the lists to numpy arrays
predictions = np.array(predictions)
image_filenames = np.array(image_filenames)

# Print the predictions and corresponding filenames
for i in range(len(predictions)):
    print(f"Filename: {image_filenames[i]}, Prediction: {predictions[i]}")

# Define the output CSV file path
output_csv_file = 'submission.csv'

# Open the CSV file in write mode
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['ID(name of the image)', 'Class(number of image)'])

    # Write the predictions and corresponding filenames
    for i in range(len(predictions)):
        # Extract only the base filename without the extension
        image_name = os.path.splitext(os.path.basename(image_filenames[i]))[0]
        # Get the predicted class number
        predicted_class = np.argmax(predictions[i])
        writer.writerow([image_name, predicted_class])

print(f"Submission file saved to {output_csv_file}")
