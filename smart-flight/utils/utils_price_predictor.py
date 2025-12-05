
import joblib
import pandas as pd

# Expect a pipeline saved as model.pkl that takes a DataFrame row with the columns:
# Airline,Source,Destination,Journey_Day,Journey_Month,Journey_Weekday,Dep_Hour,Arr_Hour,Duration_min,Total_Stops_num

MODEL_PATH = "price_model.pkl"

def load_model(path=MODEL_PATH):
    return joblib.load(path)

def predict_price(model, input_df):
    # input_df: single-row DataFrame with the same columns used in training
    pred = model.predict(input_df)
    return float(pred[0])
