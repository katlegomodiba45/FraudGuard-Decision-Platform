import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("decisions.csv")

def log_decision(amount: float, score: float, decision: str):
    is_new = not LOG_FILE.exists()
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["timestamp", "amount", "score", "decision"])
        writer.writerow([datetime.now().isoformat(), amount, score, decision])