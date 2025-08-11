import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import joblib


iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X_scaled)


centroids = []
for cluster_id in range(3):
    cluster_points = X_scaled[labels == cluster_id]
    centroids.append(cluster_points.mean(axis=0))
centroids = np.array(centroids)

joblib.dump({
    "scaler": scaler,
    "centroids": centroids,
    "features": iris.feature_names
}, "hierarchical_model.pkl")

print("Model and centroids saved successfully.")
