from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model_1 = joblib.load("model_1.pkl")
model_2 = joblib.load("model_2.pkl")
fertilizer_encoder = joblib.load("fertilizer_label_encoder.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosphorus'])
        K = float(request.form['Potassium'])
        ph = float(request.form['pH_Value'])
        temp = float(request.form['Temperature'])
        hum = float(request.form['Humidity'])
        rain = float(request.form['Rainfall'])
        carbon = float(request.form['Carbon'])
        soil = request.form['Soil']

        input_crop = pd.DataFrame([[temp, hum, rain, ph, N, P, K]], columns=['Temperature', 'Humidity', 'Rainfall', 'pH_Value', 'Nitrogen', 'Phosphorus', 'Potassium'])

        crop_predicted = model_1.predict(input_crop)[0]

        input_fertilizer = pd.DataFrame([{
            "Temperature": temp, 
            "Humidity": hum, 
            "Rainfall": rain, 
            "pH_Value": ph, 
            "Nitrogen": N, 
            "Phosphorus": P, 
            "Potassium": K,
            "Soil": soil,
            "Carbon": carbon,
            "Crop": crop_predicted
        }])

        fertilizer_number = model_2.predict(input_fertilizer)[0]
        fertilizer_predicted = fertilizer_encoder.inverse_transform([fertilizer_number])[0]
        return render_template("result.html", crop=crop_predicted, fertilizer=fertilizer_predicted)

if __name__ == "__main__":
    app.run(debug=True)