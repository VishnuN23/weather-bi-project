import schedule
import time
import subprocess
import sys

def run_etl():
    print("\nRunning Weather ETL Pipeline...")
    subprocess.run(
        [sys.executable, "scripts/weather_etl_flow.py"]
    )

schedule.every(24).hours.do(run_etl)

print("Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(1)