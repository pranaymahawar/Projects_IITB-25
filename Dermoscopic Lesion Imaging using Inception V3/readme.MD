# Dermoscopic Lesion Diagnosis

## Introduction

Dermoscopic lesion diagnosis is a challenging task in the field of dermatology due to the long-tailed distribution of clinical findings observed in dermoscopic images. This project aims to develop a diagnostic system for dermoscopic lesion imaging, addressing the challenge of class imbalance present in the dataset.

## Dataset Overview

The dataset used in this project consists of 10,015 skin images with 7 lesion classes. The dataset exhibits a significant class imbalance, with an imbalance ratio (IR) of 58. The imbalance ratio is defined as the ratio of the sample size of the largest majority class to that of the smallest minority class.

## Objectives

- Develop a multi-class diagnostic system for dermoscopic lesion images.
- Address the challenge of class imbalance in the dataset.
- Ensure the diagnostic system can accurately identify both common and rare lesion classes.
- Explore and implement methods to handle long-tailed medical image recognition problems effectively.
- Evaluate the performance of the diagnostic system using appropriate metrics and validation techniques.

## Installation

1. Clone the repository:
- git clones https://github.com/pranaymahawar/Projects_IITB-25/tree/master/Dermoscopic%20Lesion%20Imaging%20using%20Inception%20V3.git
cd dermoscopic-lesion-diagnosis

2. Install the required dependencies:

## Usage

1. Train the diagnostic model:

2. Evaluate the model performance:

3. Generate predictions for new dermoscopic images:

## File Structure

The project directory structure is as follows:

 
``` bash 
dermoscopic-lesion-diagnosis/
│
├── data/ # Directory containing dataset
│ └── images/
│ └── ... # Dermoscopic lesion images
│ └── labels.csv # CSV file containing image labels
├── models/ # Directory to save trained models
│ └── ...
├── train_model.py # Script to train the diagnostic model
├── evaluate_model.py # Script to evaluate model performance
├── predict.py # Script to generate predictions
├── requirements.txt # List of dependencies
└── README.md # Project README file
```

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
- Copyright (c) [2024] [Pranay Mahawar]
- This software is licensed under the MIT License. See LICENSE for details.


## Contact

For any questions or inquiries about this project, please contact Pranay mahawar(pranaymahawar34@gmail.com).

## Acknowledgements

- This project was developed as part of the AIML Winter Workshop organized by WNCC.
- The dataset used in this project was provided by [Dataset Provider Name](https://www.kaggle.com/competitions/aiml-general-championship/data).
- Various libraries and frameworks were used in the development of this project.

