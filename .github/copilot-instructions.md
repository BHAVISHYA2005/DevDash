# Copilot Instructions for portia-oncall-agent

## Project Purpose & Philosophy
- Automate on-call triage using Portia agents: read logs, diagnose issues, suggest solutions, and notify engineers via Slack.
- Human-in-the-loop: No fixes are executed without explicit engineer approval. Safety and auditability are prioritized.
- All tools/platforms must be free and open-source.

## Architecture Overview
- Modular design: Each function (log reading, error parsing, suggestion logic, notification, approval, audit) is a separate directory/module.
- Data flow:
	1. Log Source (`sample_logs/`): Local/sample files for simulation and testing.
	2. Log Reader (`log_reader/`): Reads logs from source.
	3. Error Parser (`error_parser/`): Detects known error patterns (regex/keywords).
	4. Suggestion Generator (`suggestion_generator/`): Maps errors to recommended fixes.
	5. Notification (`notification/`): Sends actionable messages to Slack.
	6. Human Approval: Engineers approve/decline actions via Slack.
	7. Audit (`audit/`): Logs all agent actions and decisions for compliance/debugging.
	8. Config (`config/`): Stores configuration and environment variable docs. Never hardcode secrets.

## Key Conventions & Patterns
- Each module is independent for testability and future extension.
- Use environment variables for secrets—never hardcode credentials.
- Error detection is regex/keyword-based (see `error_parser/`).
- Slack integration uses the free tier for notifications (see `notification/`).
- All agent actions must be logged for auditability (see `audit/`).
- Document new error patterns and log sources in their respective README files.

## Developer Workflows
- To test, place log files in `sample_logs/` and run the log reader.
- Debugging: Use the `audit/` module to trace agent actions and decisions.
- Configuration: Use files in `config/` and environment variables. Never hardcode secrets.
- To add new error patterns, update `error_parser/` and its README.
- To change notification behavior, update `notification/` implementation.

## Integration Points
- Portia is the core agent framework for planning, tool integration, and human approval.
- Slack is the only external service (for notifications/approvals).
- All modules communicate via well-defined interfaces and file boundaries.

## Example Workflow
1. Log file added to `sample_logs/`
2. Log Reader ingests logs
3. Error Parser matches patterns
4. Suggestion Generator proposes fixes
5. Notification sent to Slack
6. Engineer approves/declines
7. Audit logs updated

## Key Files & Directories
- `architecture.md`: High-level goals, constraints, and design rationale
- `log_reader/`, `error_parser/`, `suggestion_generator/`, `notification/`, `audit/`, `config/`, `sample_logs/`: Each contains a README with module-specific guidance

---
If anything changes, update this file and `architecture.md` accordingly. For unclear workflows, review module README files or ask for clarification.
