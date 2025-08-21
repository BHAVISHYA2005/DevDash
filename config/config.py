import os

# Configuration loader for environment variables and defaults
LOG_PATH = os.getenv('ONCALL_LOG_PATH', 'sample_logs/single_error.log')
SLACK_TOKEN = os.getenv('ONCALL_SLACK_TOKEN', None)
AUDIT_LOG_PATH = os.getenv('ONCALL_AUDIT_LOG_PATH', 'audit.log')

# Add more config variables as needed
