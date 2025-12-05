# ✈️ Smart Flight Purchase System (small project focused on integrating ML with Web)

A machine learning + Flask web application that predicts flight ticket prices and recommends:

✔ Best time to purchase  
✔ Best route  
✔ Price estimate  

Model trained in Google Colab → deployed in Flask (VS Code).

## 🚀 Features

### ✔ Price Prediction
Predicts the approximate flight ticket price using machine learning.

### ✔ Best Time to Book
Displays:
- **Best months to book**
- **Cheapest weekdays**
- **Smart booking advice**

### ✔ Route Recommendation
Suggests the best possible route based on:
- Price trend  
- Availability  
- Route score  

### ✔ Clean UI
- Responsive design  
- Light/Dark mode  
- Animated background

## 📂 Project Structure
smart-flight-prediction/smart-flight

│── app.py

│── price_model.pkl

│── processed_data_for_recommender.csv

│── requirements.txt

│── README.md

│
├── templates/

│ └── index.html

│ └── result.html

│

├── utils/

| |__ __init__.py

│ ├── utils_preprocess.py

│ ├── utils_price_predictor.py

│ ├── utils_time_recommender.py

│ ├── utils_route_recommender.py

│

└── static/

├── css/

│ └── style.css

│ └── results.css

├── js/

│ └── script.js

└── images/

└── bg_light.png

└── bg_dark.png

└── plane-ticket.png

|__ plane.png

└── clock.png

|__ customer-journey.png

---

## 🧠 ML Model
- Trained in **Google Colab**
- Preprocessed dataset → `processed_data.csv`
- Final model exported as → `model.pkl`
- Algorithm used: **Random Forest Regressor**  
  *(customizable)*

---

## ⚙️ Installation


### 1️⃣ Clone the repository
git clone https://github.com<your-username>/smart-flight-prediction.git


cd smart-flight-prediction

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the Flask app
python app.py

The app will run on:
http://127.0.0.1:5000/

🙌 Author
Sombarna Basu
Pre-Final Year B.Tech Cse Student (2025)
