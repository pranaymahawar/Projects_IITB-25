## Credit Risk Analysis

## Description
This project focuses on analyzing credit risk using machine learning techniques. It utilizes various classifiers such as Logistic Regression, Random Forest, Decision Tree, and Neural Network to predict credit risk based on a set of features extracted from credit history data. The project aims to help financial institutions assess the risk associated with extending credit to individuals or entities.

## Features
- Loads credit history data from a CSV file.
- Handles missing values by filling them with mean values.
- Splits the dataset into training and testing sets.
- Normalizes features using StandardScaler.
- Trains multiple classifiers including Logistic Regression, Random Forest, Decision Tree, and Neural Network.
- Evaluates the performance of each classifier using accuracy score and confusion matrix.
- Provides a function to predict credit risk for new data inputs.
## Usage
- Ensure Python and necessary libraries are installed (pandas, numpy, scikit-learn, joblib, gradio).
- Clone the repository or download the source code.
- Place your credit history data in CSV format and update the file path in the script.
- Run the script to preprocess the data, train classifiers, and evaluate performance.
- Use the provided function to predict credit risk for new data inputs.
## File Structure
- data.csv: Sample credit history data (replace with your own dataset).
- credit_risk_analysis.py: Main Python script containing data preprocessing, model training, evaluation, and prediction functions.
- Normalisation_Data: Saved scaler for feature normalization.
- Classifier_Model: Saved trained classifier model.
## Results
Accurary score is 0.827
## Dependencies
pandas,
numpy,
scikit-learn,
joblib,
gradio.

## License
This project is licensed under the MIT License.

This README file should provide a clear overview of the project, its dependencies, installation, usage, results, and model architecture.