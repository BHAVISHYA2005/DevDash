import re

def parse_errors(log_lines):
    """Parse errors from log lines using regex/keywords."""
    error_patterns = {
        "DatabaseError": re.compile(r"database (error|connection failed|unavailable)", re.IGNORECASE),
        "TimeoutError": re.compile(r"timeout|timed out", re.IGNORECASE),
        "DiskFull": re.compile(r"disk (full|quota exceeded)", re.IGNORECASE),
        "PermissionDenied": re.compile(r"permission denied|access denied", re.IGNORECASE),
        "ERROR": re.compile(r"ERROR", re.IGNORECASE),
        "CRITICAL": re.compile(r"CRITICAL", re.IGNORECASE),
        "WARNING": re.compile(r"WARNING", re.IGNORECASE),
    }
    detected_errors = set()
    for line in log_lines:
        for error_type, pattern in error_patterns.items():
            if pattern.search(line):
                detected_errors.add(error_type)
    return list(detected_errors)
