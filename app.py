from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


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
        soil = request.form['Soil']

        return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)