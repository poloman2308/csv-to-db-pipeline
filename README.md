# 📦 CSV-to-Database ETL Pipeline

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/poloman2308/csv-to-db-pipeline/actions)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-blue)](https://github.com/poloman2308/csv-to-db-pipeline)

A lightweight data engineering pipeline that loads CSV files into a PostgreSQL database using **Python, Pandas, SQLAlchemy**, and exposes a triggerable **Flask API**.

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

## End-to-End Flow Diagram

```mermaid
flowchart LR
  %% ---------- INGEST ----------
  subgraph Ingest
    C1[data/customers.csv] -->|CLI 🧩| L1[load_data.py<br/>--csv --table]
    C2[data/orders.csv]   -->|API 🚀| API[/POST /load<br/>app.py/]
  end

  %% ---------- TRANSFORM & LOAD ----------
  subgraph ETL Engine
    L1 --> T1[Pandas<br/>clean/transform]
    API --> T2[Pandas<br/>validate/normalize]
    T1 --> DB[(PostgreSQL<br/>raw_customers)]
    T2 --> DB
  end

  %% ---------- MONITORING ----------
  subgraph Logging
    L1 --> LOG1[(console.log 📋)]
    API --> LOG2[(Flask log 📋)]
  end

  style C1 fill:#fffbe7,stroke:#444
  style C2 fill:#fffbe7,stroke:#444
  style L1 fill:#dde1ff,stroke:#444
  style API fill:#dde1ff,stroke:#444
  style T1 fill:#e7ffe7,stroke:#444
  style T2 fill:#e7ffe7,stroke:#444
  style DB fill:#ffe7e7,stroke:#444
  style LOG1 fill:#e7f5ff,stroke:#444
  style LOG2 fill:#e7f5ff,stroke:#444
```

---

## ⚙️ .env Format

```yaml
DB_USER=dbt_user
DB_PASSWORD=dbt_pass
DB_NAME=ecommerce
DB_HOST=localhost
DB_PORT=5433
```
> 🔐 This file should be excluded from Git (.gitignore).

---

## 🖥️ Run Locally

```
python etl/load_data.py --csv data/customers.csv --table raw_customers
python etl/load_data.py --csv data/orders.csv --table raw_orders
python etl/load_data.py --csv data/products.csv --table raw_products
```

---

## ▶️ Flask API:

```bash
python api/app.py
```

---

## 🔁 Make a request:

```
curl -X POST http://localhost:5000/load \
     -H "Content-Type: application/json" \
     -d "{\"csv_path\": \"data/customers.csv\", \"table_name\": \"raw_customers\"}"
```

---

## 🐳 Optional: Start PostgreSQL via Docker

```bash
docker run --name etl-postgres -e POSTGRES_USER=dbt_user -e POSTGRES_PASSWORD=dbt_pass -e POSTGRES_DB=ecommerce -p 5433:5432 -d postgres:15
```

---

## ✅ Example Response

```json
{
  "message": "Loaded data/customers.csv into raw_customers"
}
```

---

## ✍️ Author

**Derek Acevedo**  
📍 [GitHub](https://github.com/poloman2308)  
📄 [LinkedIn](https://www.linkedin.com/in/derekacevedo86)


