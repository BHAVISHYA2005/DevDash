def generate_suggestions(errors):
    """Maps error types to actionable suggestions."""
    error_suggestion_map = {
        "SampleError": "Check system configuration and restart service.",
        "DatabaseError": "Verify database connection, credentials, and database health. Restart DB service if needed.",
        "TimeoutError": "Increase timeout, check network connectivity, and review service load.",
        "DiskFull": "Free up disk space, archive old logs, or add more storage.",
        "PermissionDenied": "Check user permissions, access rights, and security policies.",
        "NetworkError": "Check network cables, switches, and firewall rules. Restart network service if needed.",
        "MemoryError": "Restart service, check for memory leaks, and increase memory allocation if possible.",
        "ServiceCrash": "Check service logs, restart the service, and review recent changes or deployments.",
        "ERROR": "Review error logs for details and escalate if unresolved.",
        "CRITICAL": "Immediate attention required. Escalate to on-call engineer.",
        "WARNING": "Monitor the situation and review warning logs for potential issues.",
    }
    suggestions = []
    for error in errors:
        suggestion = error_suggestion_map.get(error, f"No suggestion available for: {error}")
        suggestions.append(suggestion)
    return suggestions
