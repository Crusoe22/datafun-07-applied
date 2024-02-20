# datafun-07-applied
# Project 7 Machine Learning
Nolan Moss

## Overview
This Jupyter Notebook contains a machine learning project focusing on predicting temperatures in New York City and exploring housing data in California. The project encompasses various stages of the machine learning workflow, including data acquisition, data cleaning, model building, prediction, visualization, and model evaluation.

## Table of Contents
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Part 1 - Chart a Straight Line](#part-1)
4. [Part 2 - NYC Temperature Prediction](#part-2)
   - [Section 1: Data Acquisition](#section-1---data-acquisition)
   - [Section 2: Data Inspection](#section-2---data-inspection)
   - [Section 3: Data Cleaning](#section-3---data-cleaning)
   - [Section 4: Descriptive Statistics](#section-4---descriptive-statistics)
   - [Section 5: Build the Model](#section-5---build-the-model)
   - [Section 6: Predict](#section-6---predict)
   - [Section 7: Visualizations](#section-7---visualizations)
5. [Part 3 - NYC Temperature Prediction (Continued)](#part-3)
   - [Section 1: Build the Model](#section-1---build-the-model)
   - [Section 2: Test the Model](#section-2---test-the-model)
   - [Section 3: Predict](#section-3---predict)
   - [Section 4: Visualizations](#section-4---visualizations)
6. [Part 5 - Bonus: California Housing Data](#part-4---bonus)
   - [Load the Dataset](#load-the-dataset)
   - [Exploring the Data](#exploring-the-data)
   - [Visualize the Features](#visualize-the-features)
   - [Split the Data for Training and Testing](#split-the-data-for-training-and-testing)
   - [Training the Model](#training-the-model)
   - [Testing the Model](#testing-the-model)
   - [Visualize the Expected vs. Predicted Prices](#visualize-the-expected-vs-predicted-prices)
   - [Regression Model Metrics](#regression-model-metrics)
   - [Choosing the Best Model](#choosing-the-best-model)

### Environment Setup and How to Install and Run the Project

1. Create and clone repository to VSCode
- Create a new GitHub repository named datafun-07-applied.
- Clone the repository to your local machine.

2. Create and Activate Virtual Environment
- Create a Project Virtual Environment in the .venv folder.
- Activate the Project Virtual Environment.
```console
py -m venv .venv
.\.venv\Scripts\Activate
```

3. Requirements
- Install packages 
```console
py -m pip install jupyterlab pandas matplotlib 
```
- Freeze your requirements to requirements.txt. 
```console
py -m pip install requests
py -m pip freeze > requirements.txt
```

4. Git Ignore
- Add a useful .gitignore to the root project folder.


## Introduction<a name="introduction"></a>
This Jupyter Notebook contains code and documentation for a machine learning project that predicts temperatures in New York City and explores housing data in California. The project utilizes various libraries such as `scikit-learn`, `pandas`, `seaborn`, `matplotlib`, and `numpy` for data manipulation, visualization, and modeling.

## Dependencies<a name="dependencies"></a>
- scikit-learn
- pandas
- seaborn
- matplotlib
- scipy
- numpy

## Part 1 - Chart a Straight Line<a name="part-1"></a>
This section charts the linear relationship between Fahrenheit and Celsius temperatures.

## Part 2 - NYC Temperature Prediction<a name="part-2"></a>
### Section 1 - Data Acquisition<a name="section-1---data-acquisition"></a>
The NYC temperature data is loaded from a CSV file into a Pandas DataFrame.

### Section 2 - Data Inspection<a name="section-2---data-inspection"></a>
Basic inspection of the dataset using `head()` and `tail()` functions.

### Section 3 - Data Cleaning<a name="section-3---data-cleaning"></a>
Column names are modified for clarity, and the 'Date' column is adjusted.

### Section 4 - Descriptive Statistics<a name="section-4---descriptive-statistics"></a>
Descriptive statistics are computed for the temperature data.

### Section 5 - Build the Model<a name="section-5---build-the-model"></a>
A linear regression model is built to predict NYC temperatures.

### Section 6 - Predict<a name="section-6---predict"></a>
Temperature prediction using the linear regression model.

### Section 7 - Visualizations<a name="section-7---visualizations"></a>
Visualization of NYC temperature prediction using Seaborn.

## Part 3 - NYC Temperature Prediction (Continued)<a name="part-3"></a>
Continuation of NYC temperature prediction, including model training, testing, prediction, and visualization.

## Part 5 - Bonus: California Housing Data<a name="part-4---bonus"></a>
Exploration of California housing data, including data loading, exploration, visualization, model training, testing, evaluation, and selection.

For further details and insights, please refer to the specific sections within the notebook.