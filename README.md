# 🌸 Hierarchical Clustering Web App (Iris Dataset)

This project is a **Flask-powered web application** that uses a **Hierarchical Clustering model** to group iris flowers into clusters based on their physical characteristics.  

The model is trained using the **Iris dataset** from the UCI Machine Learning Repository, which contains measurements of sepal length, sepal width, petal length, and petal width for 150 flowers.

---

## 🚀 Features
- Uses the classic, well-known **Iris dataset** for demonstration and testing.
- **4 numeric features** with clear cluster separation for meaningful predictions.
- User-friendly Flask web interface with example placeholders for quick testing.
- Predicts and displays the **cluster ID** (0, 1, or 2) for any set of inputs.

---

## 📂 Project Structure
```hierarchical-clustering-iris/
│
├── model.py # Loads dataset, trains hierarchical clustering model, saves model+scaler+features
├── app.py # Flask web app that loads model and predicts clusters
├── hierarchical_clustering_model.pkl # Saved model, scaler, and features
├── templates/
│   └── index.html # Web form UI with example placeholders
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## 🔧 Installation
1. **Clone this repository**  
```bash
git clone <your-repo-url>
cd hierarchical-clustering-iris
```
2. **Install dependencies**  
```bash
pip install -r requirements.txt
```
3. **Train the model**  
```bash
python model.py
```
4. **Run the web app**  
```bash
python app.py
```
5. **Open in Browser**  
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥 Example Inputs for Testing
Here are sample inputs that should produce different clusters:

| Cluster | Sepal Length (cm) | Sepal Width (cm) | Petal Length (cm) | Petal Width (cm) |
|---------|-------------------|------------------|-------------------|------------------|
| **0**   | `5.1`              | `3.5`            | `1.4`             | `0.2`            |
| **1**   | `6.0`              | `2.2`            | `4.0`             | `1.3`            |
| **2**   | `6.5`              | `3.0`            | `5.2`             | `2.0`            |

---

## ⚙ Requirements
Flask  
scikit-learn  
pandas  
numpy  
joblib  

---

## 📸 Screenshot

