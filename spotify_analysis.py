# --- Spotify Analysis (EDA + KMeans + Auto Cluster Naming + SQLite Integration) ---
# Run:
#   cd C:\Users\eXelixi-NB\Desktop\spotify.ai
#   python spotify_analysis.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# -----------------------------
# 1) Load data
# -----------------------------
CSV_NAME = "spotify.csv"
if not os.path.exists(CSV_NAME):
    raise FileNotFoundError(f"Δεν βρέθηκε το {CSV_NAME} στον τρέχοντα φάκελο.")
df = pd.read_csv(CSV_NAME)

print("✅ Loaded:", CSV_NAME)
print("Shape:", df.shape)

# -----------------------------
# 2) Basic cleaning
# -----------------------------
df = df.drop_duplicates()
features = [c for c in ["danceability", "energy", "valence", "tempo"] if c in df.columns]
if len(features) < 2:
    raise ValueError("Χρειάζομαι τουλάχιστον 2 από: danceability, energy, valence, tempo.")
work = df.copy().dropna(subset=features)

# -----------------------------
# 3) EDA
# -----------------------------
plt.figure(figsize=(8, 6))
sns.heatmap(work[features].corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlations.png", dpi=150)
plt.close()

if "popularity" in work.columns and "danceability" in work.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=work, x="danceability", y="popularity", hue=work.get("artist", None))
    plt.title("Danceability vs Popularity")
    plt.tight_layout()
    plt.savefig("dance_vs_pop.png", dpi=150)
    plt.close()

# -----------------------------
# 4) K-Means with silhouette
# -----------------------------
X = work[features].to_numpy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

best_k, best_score = None, -1
scores = {}
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels_tmp = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels_tmp)
    scores[k] = sil
    if sil > best_score:
        best_score = sil
        best_k = k

print(f"👉 Selected k = {best_k} (silhouette={best_score:.3f})")

kmeans = KMeans(n_clusters=best_k, n_init=10, random_state=42)
labels = kmeans.fit_predict(X_scaled)
work["cluster"] = labels

# -----------------------------
# 5) PCA 2D visualization
# -----------------------------
pca = PCA(n_components=2, random_state=42)
pts2d = pca.fit_transform(X_scaled)
work["pc1"] = pts2d[:, 0]
work["pc2"] = pts2d[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(data=work, x="pc1", y="pc2", hue="cluster", palette="tab10", s=120)
plt.title("K-Means Clusters (PCA 2D)")
plt.tight_layout()
plt.savefig("clusters_pca.png", dpi=150)
plt.close()

# -----------------------------
# 6) Auto cluster naming
# -----------------------------
centroids_df = pd.DataFrame(kmeans.cluster_centers_, columns=features)
centroids_df["cluster"] = range(best_k)

def name_cluster(row):
    hi, lo = 0.6, -0.4
    d, e, v, t = row.get("danceability",0), row.get("energy",0), row.get("valence",0), row.get("tempo",0)
    if e > hi and d > hi: return "High-Energy Dance"
    if v > hi and d > hi: return "Upbeat Pop"
    if e < lo and v < lo: return "Moody / Low Energy"
    if e < lo and t < lo: return "Chill Mellow"
    if t > hi and e > 0.3: return "Fast & Energetic"
    if d > hi and e > 0: return "Groovy"
    if v > hi and e <= 0.2: return "Bright Acoustic"
    return "Mixed / Balanced"

centroids_df["cluster_name"] = centroids_df.apply(name_cluster, axis=1)
name_map = dict(zip(centroids_df["cluster"], centroids_df["cluster_name"]))
work["cluster_name"] = work["cluster"].map(name_map)

# -----------------------------
# 7) Cluster profiling & export
# -----------------------------
profile = work.groupby("cluster")[features].mean().round(3)
counts = work["cluster"].value_counts().sort_index()
names = pd.Series(name_map, name="cluster_name")

profile_out = profile.copy()
profile_out["cluster_name"] = names
profile_out.to_csv("cluster_profile.csv")

base_cols = [c for c in ["track_name","artist","year","popularity"] if c in work.columns]
work[base_cols + features + ["cluster","cluster_name"]].to_csv("spotify_with_clusters.csv", index=False)

# -----------------------------
# 8) Save results to SQLite
# -----------------------------
DB_NAME = "spotify_analysis.db"
conn = sqlite3.connect(DB_NAME)

work.to_sql("spotify_clusters", conn, if_exists="replace", index=False)
print(f"\n✅ Saved results to database: {DB_NAME} (table: spotify_clusters)")

# Example SQL queries
q1 = pd.read_sql("SELECT cluster_name, COUNT(*) as n_tracks FROM spotify_clusters GROUP BY cluster_name", conn)
q2 = pd.read_sql("SELECT artist, AVG(popularity) as avg_pop FROM spotify_clusters GROUP BY artist ORDER BY avg_pop DESC LIMIT 5", conn)

print("\n--- Tracks per Cluster ---")
print(q1)

print("\n--- Top 5 Artists by Avg Popularity ---")
print(q2)

conn.close()

print("\n✅ Done! Created files:")
print(" - correlations.png")
if "popularity" in work.columns:
    print(" - dance_vs_pop.png")
print(" - clusters_pca.png")
print(" - cluster_profile.csv")
print(" - spotify_with_clusters.csv")
print(" - spotify_analysis.db")