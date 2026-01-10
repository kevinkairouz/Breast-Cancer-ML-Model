# Breast Cancer Detection System

A machine learning application for breast cancer diagnosis prediction using the Wisconsin Breast Cancer Dataset. Features comprehensive algorithm comparison, hyperparameter tuning, and an API built with Flask.

## Features

* **Machine Learning Model**: RandomForest classifier with optimized hyperparameters (n_estimators=100, max_depth=15)
* **Algorithm Comparison**: Systematic evaluation of 4 ML algorithms (RandomForest, DecisionTree, KNN, LogisticRegression)
* **Hyperparameter Optimization**: GridSearchCV and RandomizedSearchCV for model tuning
* **Real-time Predictions**: Interactive web interface for instant diagnosis predictions
* **ML Analysis**: Algorithm Analysis for all 4 ML algorithms with visualizations offered for the following (Recall, Score, Precision)



## Project Structure

### Branch: `model` (Python-Only)
Core machine learning analysis and model development
* `analysis.py` - Algorithm comparison and hyperparameter tuning
* `breast-cancer.csv` - Wisconsin Breast Cancer Dataset (569 samples, 30 features)

### Branch: `main` (with api)
Complete web application with Flask API
* `model.py` - Flask REST API with `/predict` endpoint
* `analysis.py` - ML algorithm evaluation script
* `breast-cancer.csv` - Training dataset

## Machine Learning Components

### Algorithms Evaluated:
* **RandomForestClassifier** - Ensemble method with multiple decision trees
* **DecisionTreeClassifier** - Single tree-based classification
* **KNeighborsClassifier** - Distance-based nearest neighbor classification
* **LogisticRegression** - Linear probabilistic classification

### Hyperparameter Tuning:
* **RandomForestClassifier**: `n_estimators` [1, 10, 100, 500, 700, 1000], `max_depth` [1, 5, 10, 15, 20, 30]
* **DecisionTreeClassifier**: `max_depth` [1, 5, 10, 15, 20, 30]
* **KNeighborsClassifier**: `n_neighbors` [5, 10, 15, 20, 25]
* **LogisticRegression**: `C` [1, 5, 15, 50, 100]

### Model Evaluation:
* **Cross-Validation**: 5-fold stratified cross-validation with `train_test_split`
* **Metrics**: Accuracy, Recall, Precision, F1-Score
* **Visualization**: 3-subplot bar chart comparing algorithm performance
* **Classification Reports**: Detailed per-class metrics for all models

## Flask API Architecture

### Backend (Flask):
* **Flask Application**: RESTful API with JSON request/response handling
* **Routing**:
  * `/` - Main page (GET) - Renders HTML form
  * `/predict` - Prediction endpoint (POST) - Accepts JSON, returns diagnosis
* **Data Processing**: 
  * JSON parsing with `request.get_json()`
  * Feature extraction in correct order using `feature_names` list
  * NumPy array conversion for model input
* **Model Training**: On-demand training within `/predict` route (development pattern)
* **Response Format**: `{"prediction": "Malignant"}` or `{"prediction": "Benign"}`

## Data Processing Pipeline

### Input Features (30 total):
* **Mean Features (10)**: radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean
* **Standard Error Features (10)**: radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se
* **Worst Features (10)**: radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst

### Data Preprocessing:
* Label encoding: "M" (Malignant) → 1, "B" (Benign) → 0
* ID column removal
* Train-test split with stratification (maintains class distribution)
* Feature ordering preservation for prediction input

## Installation & Setup

### Prerequisites:
```bash
python 3.11+
pip (Python package manager)
```

### Required Libraries:
```bash
pip install flask pandas numpy scikit-learn matplotlib
```

### Running the Application:

**ML Analysis Only:**
```bash
python analysis.py
```

**Full Web Application:**
```bash
python model.py
```
Navigate to: `http://127.0.0.1:5000/`

### Sample Data (Malignant Case):
```
17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189
```


## Advanced Features

* **Systematic Model Comparison**: Automated evaluation of 4 algorithms with hyperparameter search
* **Visual Performance Analysis**: Matplotlib bar charts comparing accuracy, recall, and precision
* **Optimized Model**: Selected RandomForest based on comprehensive evaluation


## Technical Details

### Model Performance:
* **Best Model**: RandomForest (n_estimators=100, max_depth=15)
* **Evaluation**: Accuracy, Recall, Precision metrics
* **Training**: Stratified train-test split with 75/25 ratio
* **Random State**: 42 (reproducible results)

### API Communication:
* **Request Format**: JSON with 30 feature values as floats
* **Response Format**: JSON with "prediction" key
* **HTTP Method**: POST to `/predict`
* **Content-Type**: `application/json`
