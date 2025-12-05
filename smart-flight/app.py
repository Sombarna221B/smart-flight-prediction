from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pandas as pd

# === Import Utils ===
from utils.utils_preprocess import preprocess_full_dataframe
from utils.utils_price_predictor import load_model, predict_price
from utils.utils_time_recommender import best_time_to_buy
from utils.utils_route_recommender import recommend_best_route

# === Load Model ===
model = load_model()

# === Load Dataset (Processed) ===
df = pd.read_csv("processed_data_for_recommender.csv")

app = Flask(__name__, static_folder='static', static_url_path='/static')

# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def index():
    # dropdown values
    airlines = sorted(df["Airline"].unique())
    sources = sorted(df["Source"].unique())
    destinations = sorted(df["Destination"].unique())

    return render_template(
        "index.html",
        airlines=airlines,
        sources=sources,
        destinations=destinations,
    )

# -------------------------------
# PRICE PREDICTION
# -------------------------------
@app.route("/show_results", methods=["POST"])
def show_results():
    data = request.form
    print(data)

    # --- Extract basic inputs ---
    airline = data["Airline"]
    source = data["Source"]
    destination = data["Destination"]
    stops = int(data["Total_Stops_num"])
    duration_min = int(data["Duration_min"])  # directly in minutes

    # --- Parse date ---
    date = datetime.strptime(data["Journey_Date"], "%Y-%m-%d")
    journey_day = date.day
    journey_month = date.month
    journey_weekday = date.weekday()  # Monday=0

    # --- Default departure/arrival hours ---
    dep_hour = 9                # e.g., assume 9 AM
    arr_hour = dep_hour + (duration_min // 60)

    # --- Build input row for model ---
    input_row = pd.DataFrame([{
        "Airline": airline,
        "Source": source,
        "Destination": destination,
        "Journey_Day": journey_day,
        "Journey_Month": journey_month,
        "Journey_Weekday": journey_weekday,
        "Dep_Hour": dep_hour,
        "Arr_Hour": arr_hour,
        "Duration_min": duration_min,
        "Total_Stops_num": stops
    }])
    
    #Make Predictions and Recommendations
    predicted_price = round(predict_price(model, input_row), 2)
    time_info = best_time_to_buy(df, source, destination)
    best_months = ', '.join(str(m['Journey_Month']) for m in time_info['top_months'])
    best_weekdays = ', '.join(str(w['Journey_Weekday']) for w in time_info['top_weekdays'])
    best_advice = time_info['advice'].replace('; ','\n')
    
    route_result = recommend_best_route(df, source, destination)

    #Extract route info
    if route_result:
        r = route_result[0]
        best_route_str = f"{stops} stops | {duration_min} min"
        route_score = int((1 - r['score']) * 100)
    else:
        best_route_str = "N/A"
        route_score = 0    

    return render_template(
        "result.html",
        predicted_price=predicted_price,
        best_months=best_months,
        best_weekdays=best_weekdays,
        best_advice=best_advice,
        best_route=best_route_str,
        route_score=route_score
    )
# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
