import duckdb
import pandas as pd
import os

raw_dir = "data/raw"
db_path="data/warehouse.duckdb"

def load_csv_to_duckdb(csv_filename, table_name):
    csv_path=os.path.join(raw_dir,csv_filename)

# Safety check
    if not os.path.exists(csv_path):
        print(f"Error: could not find {csv_path}")
        return

# Connect to the database
    print(f"Connecting to Duckdb at {csv_path}......")
    conn=duckdb.connect(db_path)

    print(f"Reading {csv_path} into memory")
    df=pd.read_csv(csv_path)

    print(f"Loading file into table: '{table_name}'.....")
    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
 
 # Verify the load by counting the rows
    count=conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"Success , Inserted {count} rows into the '{table_name}' table.")

    conn.close()

if __name__=="__main__":
    target_file="Car Sell Dataset.csv"

    load_csv_to_duckdb(target_file,"raw_car_sales")
