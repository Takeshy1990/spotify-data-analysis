# Spotify Data Analysis

## Overview
Ανάλυση δεδομένων από Spotify με στόχο την κατανόηση patterns στα χαρακτηριστικά των τραγουδιών.

---

## Methodology

### 1. EDA
- Καθαρισμός και διερεύνηση.
- Correlation heatmap:

![Correlation Heatmap](images/correlations.png)

- Scatter plot (Danceability vs Popularity):

![Dance vs Popularity](images/dance_vs_pop.png)

### 2. Clustering
- Επιλογή **k** με βάση silhouette score.
- Απεικόνιση clusters σε 2D μέσω PCA:

![Clusters PCA](images/clusters_pca.png)

### 3. Results
- `cluster_profile.csv`: μέσες τιμές χαρακτηριστικών ανά cluster.
- `spotify_with_clusters.csv`: πλήρες dataset με cluster label.
- SQLite database `spotify_analysis.db` + SQL queries.

### 4. Usage
```bash
python spotify_analysis.py
Project Structure
kotlin
Αντιγραφή κώδικα
/
├── data/
│   └── spotify.csv
├── images/
│   ├── correlations.png
│   ├── dance_vs_pop.png
│   └── clusters_pca.png
├── spotify_analysis.py
├── README.md
Next Steps
Πειραματισμός με dashboards (Plotly / Dash).

Ανάλυση predictive modeling (hit prediction).

Shared reporting σε HTML/PDF.

