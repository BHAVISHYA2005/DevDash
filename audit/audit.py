import datetime
from config.config import AUDIT_LOG_PATH

def log_action(action, details):
    """Log agent actions for audit (console and file)."""
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] {action}: {details}\n"
    print(f"Audit log - {action}: {details}")
    try:
        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Failed to write to {AUDIT_LOG_PATH}: {e}")
