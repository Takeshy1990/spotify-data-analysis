# 🎵 Spotify Data Analysis

## 📖 Overview
Αυτό το project κάνει **ανάλυση δεδομένων Spotify** με Python.  
Περιλαμβάνει **EDA**, **K-Means clustering**, **SQL integration**, και **visualizations**.  
Στόχος: να ανακαλύψουμε patterns στα χαρακτηριστικά τραγουδιών και να εντοπίσουμε clusters με παρόμοιο προφίλ.

---

## ⚙️ Features
- Data Cleaning (duplicates, missing values)
- Exploratory Data Analysis (EDA)
  - Correlation heatmap
  - Scatterplot (Danceability vs Popularity)
- K-Means clustering
  - Αυτόματη επιλογή του βέλτιστου `k` (silhouette score)
  - PCA 2D visualization
  - Αυτόματη ονοματοδοσία clusters (*High-Energy Dance*, *Chill Mellow*, *Upbeat Pop* κλπ.)
- Export αποτελεσμάτων
  - `cluster_profile.csv` → mean features ανά cluster
  - `spotify_with_clusters.csv` → dataset με labels
- Database Integration
  - Αποθήκευση σε SQLite (`spotify_analysis.db`)
  - Παραδείγματα SQL queries (tracks per cluster, top artists by popularity)

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Correlation Heatmap
![Correlation Heatmap](images/correlations.png)

### 🔹 Danceability vs Popularity
![Danceability vs Popularity](images/dance_vs_pop.png)

---

## 🤖 Clustering (K-Means)

Εφαρμόστηκε **K-Means clustering** με επιλογή του βέλτιστου αριθμού clusters μέσω silhouette score.  
Παράδειγμα αποτελέσματος σε 2D PCA projection:

![Clusters PCA](images/clusters_pca.png)

---

## 📂 Project Structure
spotify-data-analysis/
│
├── data/
│ └── spotify.csv
│
├── images/
│ ├── correlations.png
│ ├── dance_vs_pop.png
│ └── clusters_pca.png
│
├── spotify_analysis.py
├── cluster_profile.csv
├── spotify_with_clusters.csv
├── spotify_analysis.db
└── README.md

yaml
Αντιγραφή κώδικα

---

## ▶️ How to Run
1. Κάνε clone το repo:
   ```bash
   git clone https://github.com/YourUsername/spotify-data-analysis.git
   cd spotify-data-analysis
Εγκατέστησε dependencies:

bash
Αντιγραφή κώδικα
pip install pandas numpy matplotlib seaborn scikit-learn
Τρέξε το script:

bash
Αντιγραφή κώδικα
python spotify_analysis.py
📊 Example SQL Queries
sql
Αντιγραφή κώδικα
-- Πλήθος τραγουδιών ανά cluster
SELECT cluster_name, COUNT(*) as n_tracks
FROM spotify_clusters
GROUP BY cluster_name;

-- Top 5 καλλιτέχνες ανά μέσο popularity
SELECT artist, AVG(popularity) as avg_pop
FROM spotify_clusters
GROUP BY artist
ORDER BY avg_pop DESC
LIMIT 5;
🚀 Next Steps
Interactive dashboard (Plotly/Dash ή Power BI)

Predictive modeling (π.χ. hit prediction με βάση popularity)

Αυτόματο report σε HTML/PDF για παρουσίαση σε stakeholders

👤 Author
📌 Project by Takeshy1990 (Data Analyst in progress).

yaml
Αντιγραφή κώδικα
