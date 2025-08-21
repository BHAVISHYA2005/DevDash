def send_notification(suggestions, errors=None):
    """Format and print a notification message (simulate Slack)."""
    if errors is None:
        errors = []
    message = "\n=== Oncall Agent Notification ===\n"
    if errors:
        message += "Detected Errors:\n"
        for err in errors:
            message += f"- {err}\n"
    if suggestions:
        message += "Suggested Actions:\n"
        for sug in suggestions:
            message += f"- {sug}\n"
    message += "\nPlease review and approve/decline in Slack."
    print(message)
