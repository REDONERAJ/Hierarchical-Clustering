from flask import Flask, render_template, request
import joblib
import numpy as np

# Load saved model data
model_data = joblib.load("hierarchical_model.pkl")
scaler = model_data["scaler"]
centroids = model_data["centroids"]
features = model_data["features"]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            values = [float(request.form.get(f)) for f in features]
            values_scaled = scaler.transform([values])
            # Find nearest centroid
            distances = np.linalg.norm(centroids - values_scaled, axis=1)
            cluster = np.argmin(distances)
            prediction = f"Cluster {cluster}"
        except:
            prediction = "Invalid input"
    return render_template("index.html", features=features, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
