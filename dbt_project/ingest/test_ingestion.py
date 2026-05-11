import duckdb
import pytest

@pytest.fixture
def db_conn():
    conn=duckdb.connect("data/warehouse.duckdb")
    yield conn
    conn.close()

def test_row_count(db_conn):
    count = db_conn.execute("SELECT COUNT(*) FROM raw_car_sales").fetchone()[0]
    assert count == 140904,f"Data Loss! Expected 140904 but found {count}"

def test_columns(db_conn):
    columns = []
    data = db_conn.execute("DESCRIBE raw_car_sales").fetchall()
    for col in data:
        columns.append(col[0])
    
    required_columns = ["Brand", "Fuel Type", "State", "Year", "Owner"]

    for col in required_columns:
        assert col in columns, f"Column '{col}' not found. Check for spaces or casing"

def test_fuel(db_conn):
    rows=[]
    results=db_conn.execute("SELECT DISTINCT \"Fuel Type\" FROM raw_car_sales").fetchall()
    for row in results:
        rows.append(row[0])
    
    required_fuel=["Petrol", "Diesel", "Hybrid", "Electric"]

    for fuel_type in required_fuel:
        assert fuel_type in rows, f"Value '{fuel_type}' missing. Check if data is (lowercase) instead."
