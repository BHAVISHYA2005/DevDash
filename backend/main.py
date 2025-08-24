"""
Main entry point for Portia Oncall Agent MVP
"""
from log_reader.log_reader import read_log_file
from error_parser import error_parser
from suggestion_generator import suggestion_generator
from notification import notification
from audit import audit
from config.config import LOG_PATH

def main():
    # Step 1: Read log
    log_lines = read_log_file(LOG_PATH)
    audit.log_action('log_read', {'file': LOG_PATH, 'lines': len(log_lines)})

    # Step 2: Parse errors
    errors = error_parser.parse_errors(log_lines)
    audit.log_action('error_parsed', {'errors': errors})

    # Step 3: Generate suggestions
    suggestions = suggestion_generator.generate_suggestions(errors)
    audit.log_action('suggestions_generated', {'suggestions': suggestions})

    # Step 4: Notify (simulate Slack)
    notification.send_notification(suggestions, errors)
    audit.log_action('notification_sent', {'suggestions': suggestions, 'errors': errors})

    # Step 5: Human approval (mocked)
    approved = human_approval()
    audit.log_action('human_approval', {'approved': approved})

    if approved:
        print('Action approved. Proceeding with fix (not implemented).')
        audit.log_action('fix_executed', {})
    else:
        print('Action declined. Escalating.')
        audit.log_action('fix_declined', {})

def human_approval():
    """Simulate human approval. Replace with Slack logic later."""
    response = input("Approve suggested actions? (y/n): ").strip().lower()
    return response == 'y'

if __name__ == '__main__':
    main()
# We can add more steps here for additional processing or error handling. Duping it for later on addition.