"""
Portia Agent Orchestration for Oncall Workflow
"""
from portia import Portia, default_config
from portia.tool import Tool
from dotenv import load_dotenv
from log_reader.log_reader import read_log
from error_parser.error_parser import parse_errors
from suggestion_generator.suggestion_generator import generate_suggestions
from notification.notification import send_notification
from audit.audit import log_action
from config.config import LOG_PATH

load_dotenv()

class LogReaderTool(Tool):
    id: str = "log_reader"
    name: str = "Log Reader"
    description: str = "Reads log lines from the specified log file."
    output_schema: type = list
    def run(self, log_path=LOG_PATH):
        log_lines = read_log(log_path)
        log_action('log_read', {'file': log_path, 'lines': len(log_lines)})
        return log_lines

class ErrorParserTool(Tool):
    id: str = "error_parser"
    name: str = "Error Parser"
    description: str = "Parses errors from log lines."
    output_schema: type = list
    def run(self, log_lines):
        errors = parse_errors(log_lines)
        log_action('error_parsed', {'errors': errors})
        return errors

class SuggestionGeneratorTool(Tool):
    id: str = "suggestion_generator"
    name: str = "Suggestion Generator"
    description: str = "Generates actionable suggestions for detected errors."
    output_schema: type = list
    def run(self, errors):
        suggestions = generate_suggestions(errors)
        log_action('suggestions_generated', {'suggestions': suggestions})
        return suggestions

class NotificationTool(Tool):
    id: str = "notification"
    name: str = "Notification"
    description: str = "Sends notifications to Slack."
    output_schema: type = dict
    def run(self, suggestions, errors):
        send_notification(suggestions, errors)
        log_action('notification_sent', {'suggestions': suggestions, 'errors': errors})
        return {}

class AuditTool(Tool):
    id: str = "audit"
    name: str = "Audit"
    description: str = "Logs agent actions for auditability."
    output_schema: type = dict
    def run(self, action, details):
        log_action(action, details)
        return {}

tools = [LogReaderTool(), ErrorParserTool(), SuggestionGeneratorTool(), NotificationTool(), AuditTool()]

if __name__ == "__main__":
    portia = Portia(tools=tools, config=default_config())
    plan_run = portia.run('Run oncall triage workflow')
    print(plan_run.model_dump_json(indent=2))
