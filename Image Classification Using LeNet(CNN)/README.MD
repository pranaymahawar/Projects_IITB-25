## LeNet on MNIST with PyTorch

This project implements the LeNet architecture using PyTorch for the MNIST dataset. LeNet is a classic convolutional neural network (CNN) designed for handwritten digit recognition. The code includes the model definition, data transformations, training loop, and testing loop.

## Dependencies

- PyTorch
- torchvision

## Installation

1. Clone this repository.

2. Install the dependencies using pip.
```bash
pip install -r requirements.txt
```

## Usage
- Run the training script.
```bash
python train.py
```
- Run the testing script.
```bash
python test.py
```
The training script will display the training loss for each epoch. The testing script will display the test accuracy.

## Results
After 10 epochs of training, the test accuracy of the model is approximately 99%.

## Model Architecture
The model consists of the following layers:

Two convolutional layers with 6 and 16 filters, respectively.
Two max-pooling layers with 2x2 kernel sizes.
Three fully connected layers with 120, 84, and 10 outputs, respectively.
The model uses the ReLU activation function for the hidden layers and the Cross Entropy Loss function for training. The model is trained for 10 epochs using the Adam optimizer with a learning rate of 0.001.

Dataset
The MNIST dataset is a collection of 60,000 28x28 grayscale images of handwritten digits. There are 10,000 images in the test set and 50,000 images in the training set.

The images are preprocessed by converting them to tensors and normalizing their pixel values.

## License
This project is licensed under the MIT License.

This README file should provide a clear overview of the project, its dependencies, installation, usage, results, and model architecture.
