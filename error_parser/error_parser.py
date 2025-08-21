import re

def parse_errors(log_lines):
    """Parse errors from log lines using regex/keywords."""
    error_patterns = {
        "DatabaseError": re.compile(r"database (error|connection failed|unavailable|crash|timeout)", re.IGNORECASE),
        "TimeoutError": re.compile(r"timeout|timed out|response timed out|request timed out", re.IGNORECASE),
        "DiskFull": re.compile(r"disk (full|quota exceeded|space low|out of space)", re.IGNORECASE),
        "PermissionDenied": re.compile(r"permission denied|access denied|unauthorized|forbidden", re.IGNORECASE),
        "NetworkError": re.compile(r"network (error|unreachable|down|failure|disconnect)", re.IGNORECASE),
        "MemoryError": re.compile(r"memory (error|low|leak|exceeded|out of memory)", re.IGNORECASE),
        "ServiceCrash": re.compile(r"service (crash|stopped|unavailable|not responding)", re.IGNORECASE),
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
