import json
from datetime import datetime, timezone
import os

LOG_FILE = "data/user_logs.json"

def append_log(entry: dict):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **entry
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r+") as f:
        data = json.load(f)
        data.append(log_entry)
        f.seek(0)
        json.dump(data, f, indent=2)
