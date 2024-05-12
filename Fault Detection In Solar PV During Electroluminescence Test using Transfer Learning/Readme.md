# Fault Detection In Solar PV During Electroluminescence Test using Transfer Learning

## Introduction

Solar photovoltaic (PV) panels are critical components of renewable energy systems, and ensuring their quality is paramount for efficient energy production. Electroluminescence (EL) testing is a non-destructive technique used to detect defects within PV panels, such as microcracks, delamination, and soldering issues. This project focuses on developing a robust fault detection system for solar PV panels during EL testing using transfer learning techniques.

## Data Exploration

### Dataset Description

The dataset consists of electroluminescence images of solar PV panels, acquired through EL testing. Each image is accompanied by a label indicating the presence or absence of defects. The labels are binary, where 1 represents a defective panel and 0 represents a non-defective panel.

### Data Preprocessing

- Grayscale images are converted to RGB format to align with model input requirements.
- Categorical labels are encoded into numerical values for model compatibility.
- Data augmentation techniques are applied to enrich the training dataset and improve model generalization. Augmentation includes rotation, flipping, zooming, and shear transformations.

## Model Building

### Transfer Learning Models

1. **EfficientNetV2B2**:

```bash
pip install tf-models-official
from official.vision.image_classification import model_factory
model = model_factory.create('efficientnetv2-b2', num_classes=2)
```

2. **ResNet 50**
```import tensorflow as tf
base_model = tf.keras.applications.ResNet50(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
```
3. **VGG 16**
```base_model = tf.keras.applications.VGG16(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
```

### Training Strategy

- Transfer learning is employed, where pre-trained models are initialized with weights from ImageNet and fine-tuned for the specific task of fault detection in solar PV panels.
- Custom classification heads are added to the base models, followed by appropriate activation functions and output layers.
- Class weights are applied to address class imbalance, ensuring equitable learning from both defective and non-defective samples.

## Training and Evaluation

- The dataset is split into training and validation sets using stratified sampling to preserve class distribution.
- Data generators are utilized for efficient batch processing and augmentation during training.
- Model training is performed with dynamic learning rate scheduling, early stopping, and model checkpointing.
- Evaluation metrics such as accuracy, precision, recall, and F1 score are computed to assess model performance.
- Confusion matrices and classification reports are generated to analyze model predictions and identify potential areas for improvement.

## Visualization of Predictions

- Sample images from defective and non-defective panels are selected for visualization.
- Preprocessing steps, including resizing and normalization, are applied to prepare images for inference.
- Model predictions are made on the selected images, and visualizations are generated to compare predicted labels with ground truth labels.

## Conclusion

This project demonstrates the efficacy of transfer learning in developing a robust fault detection system for solar PV panels during electroluminescence testing. By leveraging pre-trained CNN models and customizing them for the specific task, we achieve accurate and reliable defect detection, contributing to the quality assessment of solar energy systems.

## Acknowledgments

- Special thanks to [insert names or organizations here] for providing the dataset and resources necessary for this project.
- We acknowledge the contributions of the open-source community and the developers of TensorFlow and Keras for their invaluable tools and libraries.

## Usage

To reproduce the results of this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Run the provided Python scripts for data preprocessing, model building, training, and evaluation.
4. Customize the code and experiment with different hyperparameters and architectures to optimize performance for your specific dataset and requirements.

# Requirements.txt

- tensorflow==2.7.0

- numpy==1.21.5

- pandas==1.3.5

- matplotlib==3.4.3

- scikit-learn==0.24.2

- tf-models-official==2.6.0



