from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

LOG_PATH = os.getenv('ONCALL_LOG_PATH', 'sample_logs/single_error.log')
SLACK_TOKEN = os.getenv('ONCALL_SLACK_TOKEN')
AUDIT_LOG_PATH = os.getenv('ONCALL_AUDIT_LOG_PATH', 'audit.log')
