from config.config import SLACK_TOKEN
import os

def send_notification(suggestions, errors=None):
    """Send notification to Slack if configured, else print."""
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

    slack_channel = os.getenv('ONCALL_SLACK_CHANNEL')
    if SLACK_TOKEN and slack_channel:
        try:
            from slack_sdk import WebClient
            client = WebClient(token=SLACK_TOKEN)
            client.chat_postMessage(channel=slack_channel, text=message)
            print("Notification sent to Slack.")
        except Exception as e:
            print(f"Failed to send Slack notification: {e}")
            print(message)
    else:
        print(message)
