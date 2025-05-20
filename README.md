# 📦 CSV-to-Database ETL Pipeline

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/poloman2308/csv-to-db-pipeline/actions)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-blue)](https://github.com/poloman2308/csv-to-db-pipeline)

> A lightweight data engineering pipeline that loads CSV files into a PostgreSQL database using **Python, Pandas, SQLAlchemy**, and exposes a triggerable **Flask API**.

---

## 🚀 Features

- CLI and API-based CSV ingestion
- Data transformation via Pandas
- Loads into PostgreSQL using SQLAlchemy
- Logging for all ETL events
- `.env`-based configuration
- Containerized PostgreSQL support via Docker

---

## 🧱 Project Structure

```plaintext
csv_to_db_pipeline/
├── api/               # Flask API to trigger pipeline
│   └── app.py
├── etl/               # Core ETL logic
│   └── load_data.py
├── data/              # Sample or target CSV files
├── test_request.py    # Script to test the API locally
├── .env               # DB connection credentials (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ .env Format

```
DB_USER=dbt_user
DB_PASSWORD=dbt_pass
DB_NAME=ecommerce
DB_HOST=localhost
DB_PORT=5433
```

---

## 🖥️ Run Locally

```
python etl/load_data.py --csv data/customers.csv --table raw_customers
python etl/load_data.py --csv data/orders.csv --table raw_orders
python etl/load_data.py --csv data/products.csv --table raw_products
```

---

## ▶️ API:

```
python api/app.py
```

---

## Trigger with curl:

```
curl -X POST http://localhost:5000/load \
     -H "Content-Type: application/json" \
     -d "{\"csv_path\": \"data/customers.csv\", \"table_name\": \"raw_customers\"}"
```

---

## ✍️ Author

**Derek Acevedo**  
📍 [GitHub](https://github.com/poloman2308)  
📄 [LinkedIn](https://www.linkedin.com/in/derekacevedo86)


