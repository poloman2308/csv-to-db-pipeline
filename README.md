# 📦 CSV-to-Database ETL Pipeline

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
└── README.md```

---

## ⚙️ .env Format

```
DB_USER=dbt_user
DB_PASSWORD=dbt_pass
DB_NAME=ecommerce
DB_HOST=localhost
DB_PORT=5433```

## 🖥️ Run Locally

```
python etl/load_data.py --csv data/customers.csv --table raw_customers```

## ▶️ API:

```
python api/app.py```

## Trigger with curl:

```
curl -X POST http://localhost:5000/load \
     -H "Content-Type: application/json" \
     -d "{\"csv_path\": \"data/customers.csv\", \"table_name\": \"raw_customers\"}"```

## ✍️ Author

**Derek Acevedo**  
📍 [GitHub](https://github.com/poloman2308)  
📄 [LinkedIn](https://www.linkedin.com/in/derekacevedo86)


