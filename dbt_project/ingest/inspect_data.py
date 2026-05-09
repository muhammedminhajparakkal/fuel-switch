import duckdb

# Connecting to warehouse i created
db_path= "data/warehouse.duckdb"
conn=duckdb.connect(db_path)

print(f"----Raw Data Inspection: {db_path}----")

# Check Row Count
row_count= conn.execute("SELECT COUNT(*) FROM raw_car_sales").fetchone()[0]
print(f"Total Rows Ingested: {row_count}")

# Check Column Names
columns= conn.execute("DESCRIBE raw_car_sales").fetchall()
print("\nDetected Columns:")
for col in columns:
    print(f" - {col[0]} ({col[1]})")

# Check Fuel Type Distribution
print("\nRaw Fuel Type Count : " )
fuel_summary=conn.execute("SELECT \"Fuel Type\", COUNT(*) FROM raw_car_sales GROUP BY 1").fetchall()
for fuel,count in fuel_summary:
    print(f"-{fuel}:{count}")

conn.close()


    