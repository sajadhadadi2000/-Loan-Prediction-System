import pickle
import numpy as np 
import pandas as pd
import tensorflow 

def predict(data):

    loaded_model = tensorflow.keras.models.load_model("./Model/my_model.keras")

    # load standard scaler
    with open('./Model/scaler.h5', 'rb') as f:
        scaler = pickle.load(f)

    # load label encoder
    with open('./Model/label_encoder.h5', 'rb') as f:
        label_encoder = pickle.load(f)


    # Convert to DataFrame for easier processing
    data = pd.DataFrame([data], columns=['credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
       'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
       'inq.last.6mths', 'delinq.2yrs', 'pub.rec'])


    data["purpose"] = label_encoder.transform(data["purpose"])
    data_scaled = scaler.transform(data.values)


    pred = np.argmax(loaded_model.predict(data_scaled), axis=1)[0]

    if pred == 0:
        result = """Based on the F1 score, our model predicts with 92% confidence that the customer with the entered information can pay the loan. This high accuracy indicates strong reliability in our ability to assess creditworthiness. Factors such as income, credit history, and other financial indicators contribute to this prediction. Therefore, we can make informed lending decisions, reducing the risk of defaults and enhancing overall financial stability."""
    else:
        result = """Based on the F1 score, our model predicts with 92% confidence that the customer with the entered information can not pay the loan. This high level of accuracy suggests the customer may pose a higher risk of defaulting. Key factors such as income instability, poor credit history, and other financial indicators contribute to this prediction. It is crucial to consider these insights when making lending decisions to mitigate potential losses and ensure the bank's financial health."""

    return [pred, result]



