def generate_suggestions(errors):
    """Maps error types to actionable suggestions."""
    error_suggestion_map = {
        "SampleError": "Check system configuration and restart service.",
        "DatabaseError": "Verify database connection and credentials.",
        "TimeoutError": "Increase timeout or check network connectivity.",
        "DiskFull": "Free up disk space or add more storage.",
        "PermissionDenied": "Check user permissions and access rights.",
    }
    suggestions = []
    for error in errors:
        suggestion = error_suggestion_map.get(error, f"No suggestion available for: {error}")
        suggestions.append(suggestion)
    return suggestions
