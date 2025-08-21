"""
Main entry point for Portia Oncall Agent MVP
"""
from log_reader.log_reader import read_log
from error_parser import error_parser
from suggestion_generator import suggestion_generator
from notification import notification
from audit import audit
import os

LOG_PATH = os.path.join('sample_logs', 'single_error.log')  # Example log file

def main():
    # Step 1: Read log
    log_lines = read_log(LOG_PATH)
    audit.log_action('log_read', {'file': LOG_PATH, 'lines': len(log_lines)})

    # Step 2: Parse errors
    errors = error_parser.parse_errors(log_lines)
    audit.log_action('error_parsed', {'errors': errors})

    # Step 3: Generate suggestions
    suggestions = suggestion_generator.generate_suggestions(errors)
    audit.log_action('suggestions_generated', {'suggestions': suggestions})

    # Step 4: Notify (simulate Slack)
    notification.send_notification(suggestions)
    audit.log_action('notification_sent', {'suggestions': suggestions})

    # Step 5: Human approval (mocked)
    approved = True  # Replace with real approval logic
    audit.log_action('human_approval', {'approved': approved})

    if approved:
        print('Action approved. Proceeding with fix (not implemented).')
        audit.log_action('fix_executed', {})
    else:
        print('Action declined. Escalating.')
        audit.log_action('fix_declined', {})

if __name__ == '__main__':
    main()
