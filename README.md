# Warehouse Robotics Efficiency Analyzer

This project analyzes robot pick-and-place efficiency in a simulated warehouse layout using batch logs uploaded to AWS S3 and visualized in Tableau.

---

## Features

- Tableau dashboards: congestion heatmap, delay distribution, efficiency score
- AWS S3 integration: batch uploads mimic real-time CI ingestion
- Scalable simulation: generate new batches easily with `generator.py`

---

## Workflow

1. Upload batch CSVs to S3
2. Run `s3_ingest_and_merge.py` to update `combined_batches.csv`
3. Tableau dashboard (reading this file) refreshes visual insights
4. Repeat every time a new batch arrives

---

## Tools Used

- Tableau Public (Dashboards)
- AWS S3
- Python 3 (pandas, boto3)

---

## Dashboard Previews

View Report [here](https://github.com/supzi-del/warehouse-efficiency/blob/main/Warehouse%20Robotics%20Efficiency%20Analyzer%20(Tableau%20Edition).pdf).

*(Insert images or link to screenshots)*


