# Loan Prediction System

A sophisticated web application built with Streamlit that predicts loan payment probability using deep learning.

## Overview

This project implements a machine learning model to predict whether a loan applicant will fully pay their loan based on various financial and personal indicators. The system provides a user-friendly interface for both individual predictions and batch processing through CSV file uploads.

## Features

- **Interactive Web Interface**: Clean and intuitive UI built with Streamlit
- **Dual Input Methods**:
  - Manual data entry for individual predictions
  - Batch processing via CSV file upload
- **Real-time Predictions**: Instant feedback on loan payment probability
- **High Accuracy**: 92% F1 score for prediction accuracy
- **Downloadable Results**: Export batch predictions to CSV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sajadhadadi2000/Loan-Prediction-System.git
cd loan-streamlit
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

### Manual Input
1. Navigate to the "Prediction" page
2. Select "Manual Input"
3. Fill in the required financial information
4. Click "Predict" to get the result

### Batch Processing
1. Navigate to the "Prediction" page
2. Select "Upload CSV File"
3. Upload your CSV file with the required columns
4. Click "Predict" to process all entries
5. Download the results using the "Download CSV" button

## Required CSV Format

Your CSV file should include the following columns:
- credit.policy
- purpose
- int.rate
- installment
- log.annual.inc
- dti
- fico
- days.with.cr.line
- revol.bal
- revol.util
- inq.last.6mths
- delinq.2yrs
- pub.rec

## Model Information

The system uses a deep learning model built with TensorFlow, featuring:
- Standard scaling for numerical features
- Label encoding for categorical variables
- Neural network architecture optimized for binary classification
- 92% F1 score accuracy

## Project Structure

```
loan-streamlit/
├── app.py              # Main Streamlit application
├── prediction.py       # Prediction logic and model handling
├── utils.py           # Utility functions
├── Model/             # Contains trained models
│   ├── my_model.keras
│   ├── scaler.h5
│   └── label_encoder.h5
├── static/            # Static assets
└── Output/            # Directory for batch prediction outputs
```

## License

This project is licensed under the GNU General Public License.
