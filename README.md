# 🎵 Spotify Dataset Analysis

## 📖 Overview
This project performs **Exploratory Data Analysis (EDA)**, **clustering**, and **SQL integration** on a Spotify dataset.  
It is designed as a **mid-level data analyst portfolio project**, showcasing skills in data cleaning, visualization, machine learning, and database management.

---

## ⚙️ Features
- Data cleaning (duplicates, missing values)
- Exploratory Data Analysis (EDA)
  - Correlation heatmap
  - Scatterplots (Danceability vs Popularity)
- K-Means clustering
  - Automatic selection of optimal `k` via silhouette score
  - PCA 2D visualization of clusters
  - Automatic cluster naming (e.g., *High-Energy Dance*, *Chill Mellow*)
- Export results
  - `cluster_profile.csv`: mean features per cluster
  - `spotify_with_clusters.csv`: full dataset with cluster labels
- Database integration
  - Results stored in SQLite (`spotify_analysis.db`)
  - Example SQL queries (tracks per cluster, top artists by popularity)

---

## 📂 Project Structure
spotify.ai/
│
├── spotify.csv # Input dataset
├── spotify_analysis.py # Main Python script
│
├── correlations.png # Correlation heatmap
├── dance_vs_pop.png # Scatterplot (if popularity column exists)
├── clusters_pca.png # PCA visualization of clusters
│
├── cluster_profile.csv # Summary of clusters
├── spotify_with_clusters.csv # Labeled dataset
├── spotify_analysis.db # SQLite database with results

yaml
Αντιγραφή κώδικα

---

## 🛠️ Tech Stack
- **Python** (pandas, numpy, matplotlib, seaborn, scikit-learn)
- **SQLite** (sqlalchemy, sqlite3)
- **Environment**: Anaconda + Notepad++ (or Jupyter/VSCode)

---

## ▶️ How to Run
1. Clone or download the project folder.
2. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
Run the script:

bash
Αντιγραφή κώδικα
cd path/to/spotify.ai
python spotify_analysis.py
Results will be generated in the same folder.

📊 Example Insights
Cluster analysis identifies segments such as:

High-Energy Dance: Tracks with high energy and danceability.

Chill Mellow: Low tempo & low energy acoustic tracks.

Upbeat Pop: High valence & danceability.

SQL queries allow quick business-style questions, e.g.:

“How many tracks belong to each cluster?”

“Which artists have the highest average popularity?”

🚀 Next Steps
Add a dashboard (Plotly/Dash or Power BI) for interactive exploration.

Extend analysis with predictive models (e.g., hit prediction).

Automate HTML/PDF reporting for stakeholders.

