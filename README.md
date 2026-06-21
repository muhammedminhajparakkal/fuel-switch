# 🚗 The Fuel Switch: India Automobile Market Transition
An end-to-end data engineering pipeline and analytics dashboard built on a Kaggle dataset of
Indian used car sales — demonstrating a complete DE stack from raw ingestion to an interactive
Streamlit dashboard.

> **Portfolio project** | Python · SQL · DuckDB · dbt · Streamlit · Plotly Express

## 📌 Project Overview
This project ingests, transforms and visualises vehicle registration data to answer:
- How is India's fuel mix shifting year over year?
- Which states are leading EV adoption?
- Which OEM brands are dominating the EV segment?

The result is a three-tab interactive Streamlit dashboard backed by a fully tested dbt
transformation pipeline.

### 🔄 The pipeline:
+ Loads raw CSV data into DuckDB
+  Validates data quality using pytest
+  Transforms data using dbt
+  Builds analytical marts
+  Visualizes insights in a Streamlit dashboard

## 🏗️ Architecture

```text
Raw CSV Data (Manually downloaded CSV from Kaggle)
      │
      ▼
 DuckDB
      │
      ▼
 dbt Staging
      │
      ▼
 dbt Intermediate
      │
      ▼
 dbt Marts
      │
      ▼
 Streamlit Dashboard
```
<img width="1835" height="770" alt="lineage graph" src="https://github.com/user-attachments/assets/e82d4a9b-be11-400d-b8e5-4fbd1fae084c" />


## 🛠️ Tech Stack

- Programming language - Python
- Query Language - SQL
- Database - DuckDB
- Transformation - dbt
- Testing - pytest, dbt schema tests
- Dashboard - Streamlit + Plotly Express
- Version Control - Git

## 🧪 Data Quality
- Raw layer validation using pytest
- dbt schema tests on staging models
- dbt schema tests on mart models

## 📊 Dashboard Preview
### Tab 1 — Fuel Mix Trends
Year-over-year market share distribution by fuel type with YoY growth KPI cards.
<img width="1917" height="1070" alt="Tab-1" src="https://github.com/user-attachments/assets/3a89bbf0-6b30-4724-b25c-236bec0b2c4b" />

### Tab 2 — State EV Penetration
Regional EV adoption leaderboard filtered by registration year.
<img width="1889" height="1067" alt="Tab-2" src="https://github.com/user-attachments/assets/b8980b55-b28f-4e31-83a2-ad8135f6c590" />

### Tab 3 — Maker EV Share
Automaker competitive landscape — EV market segment share by manufacturer from 2000-2023.
<img width="1873" height="1032" alt="Tab-3" src="https://github.com/user-attachments/assets/d79e58b5-f11e-4a0d-932d-4b8c7781a3f6" />

## ▶️ How to Run

```bash
# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Activate environment (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Load raw data
python ingest/load_data.py

# Run tests
pytest ingest/test_ingestion.py

# Run dbt transformations
cd dbt_project
dbt run
dbt test

# Launch dashboard
cd ..
streamlit run dashboard/app.py
```
## 💡 Key Learnings
- Designed a four-layer dbt model (raw → staging → intermediate → mart) to separate concerns and make transformations easier to debug and extend.
- Learned that catching data quality issues at the raw layer with pytest prevents silent errors from propagating into analytical models.
- Adopted Conventional Commits to keep git history readable — useful when revisiting decisions weeks later.
- Used DuckDB as a lightweight embedded warehouse instead of a cloud DB, reducing setup friction for local development.

--- 

## 📄 Data Source
[Indian Car Sell Dataset](https://www.kaggle.com/datasets/milapgohil/car-dataset) by Milap Gohil · Kaggle | License: Apache 2.0
> ⚠️ **Dataset Note:** This dataset covers **second-hand car sales**, not new vehicle registrations. The dashboard visualisations are built to demonstrate a complete data engineering pipeline — the analytical outputs reflect the used car market and should not be interpreted as real-world EV adoption or new vehicle registration trends.
 
---
