import os
import argparse
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl_pipeline.log"),
        logging.StreamHandler()
    ]
)

# Load Environment Variables
load_dotenv()

db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
         f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(db_url)

# Load Function
def load_csv_to_db(file_path, table_name):
    try:
        logging.info(f"Reading file: {file_path}")
        df = pd.read_csv(file_path)
        df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

        logging.info(f"Loading data into table: {table_name}")
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"✅ Successfully loaded {len(df)} records into '{table_name}'")
    except FileNotFoundError:
        logging.error(f"❌ File not found: {file_path}")
    except SQLAlchemyError as e:
        logging.error(f"❌ Database error: {e}")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")

# CLI Entry Point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load a CSV file into a PostgreSQL table.")
    parser.add_argument('--csv', required=True, help="Path to the CSV file (e.g., data/customers.csv)")
    parser.add_argument('--table', required=True, help="Name of the target SQL table (e.g., raw_customers)")
    args = parser.parse_args()

    load_csv_to_db(args.csv, args.table)
