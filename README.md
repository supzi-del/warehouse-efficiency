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

<img width="1192" alt="Screenshot 2025-04-05 at 8 24 36 PM" src="https://github.com/user-attachments/assets/47e3ad73-a494-4ecb-b412-394e9b1179db" />

<img width="1217" alt="Screenshot 2025-04-05 at 8 28 40 PM" src="https://github.com/user-attachments/assets/d4196080-ec5a-4924-a6e8-cbb61ee6bc0b" />

<img width="1126" alt="Screenshot 2025-04-06 at 10 06 06 AM" src="https://github.com/user-attachments/assets/e8ce529b-7651-4d16-ab66-c64f1a6c58c2" />

<img width="565" alt="Screenshot 2025-04-06 at 10 20 15 AM" src="https://github.com/user-attachments/assets/0539d438-1d1d-457a-927d-07bda8273e2d" />






