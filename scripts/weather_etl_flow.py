import subprocess
import sys

print("=== STEP 1: EXTRACT ===")
subprocess.run([sys.executable, "scripts/extract_weather.py"])

print("=== STEP 2: LOAD ===")
subprocess.run([sys.executable, "scripts/load_to_sqlite.py"])

print("=== STEP 3: REPORT ===")
subprocess.run([sys.executable, "scripts/query_database.py"])

print("=== ETL COMPLETED ===")