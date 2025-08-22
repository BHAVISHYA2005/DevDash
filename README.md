## Secret Management
Never commit your Slack token or channel ID to source code or GitHub. Store secrets in environment variables or a `.env` file (add `.env` to `.gitignore`).


# Portia Oncall Agent

## Overview
Portia Oncall Agent automates log triage for oncall engineers. It reads logs, detects errors, suggests fixes, and notifies the team via Slack, with human approval for all automated actions. All actions are logged for auditability and compliance.

## Key Features
- Modular architecture: log reading, error parsing, suggestion generation, notification, approval, and audit are separate modules.
- Regex/keyword-based error detection for reliability and extensibility.
- Actionable suggestions mapped to detected errors.
- Slack integration for real-time notifications (coming soon).
- Human-in-the-loop approval for safety.
- Persistent audit logging of all actions.

## Setup
1. Clone the repository.
2. Install Python 3.7+.
3. Create and activate a virtual environment:
	```sh
	python3 -m venv venv
	source venv/bin/activate  # or source venv/bin/activate.fish for fish shell
	```
4. Install required packages:
	```sh
	pip install slack_sdk
	```
5. Set environment variables as needed (see `config/README.md`).
6. Place sample log files in `sample_logs/`.
7. Run the agent:
	```sh
	python3 main.py
	```

## Demo Steps
1. The agent reads a sample log file and detects errors.
2. Actionable suggestions are generated for each error.
3. A notification is printed (and will be sent to Slack in future versions).
4. Human approval is requested interactively.
5. All actions are logged to `audit.log` for traceability.

## Why This Matters
This agent saves engineers from unnecessary night-time disruptions, ensures safety by requiring human approval, and provides a fully auditable workflow. It is designed for real-world impact and extensibility.

## Hackathon Value
- Demonstrates real-world automation, safety, and auditability.
- Modular and extensible for future improvements (Portia, Slack, more error patterns).
- Easy to set up and demo for judges.

## Next Steps
- Expand error patterns and suggestions.
- Integrate Slack API for notifications.
- Add Portia agent orchestration.

---
For architecture details, see `architecture.md`. For configuration, see `config/README.md`.

Portia Oncall Agent — Progress & Next Steps

Current State:

Modular agent workflow: log reading, error parsing, suggestion generation, Slack notification, human approval, audit logging.
Slack integration works via .env file and python-dotenv.
All secrets are managed securely (not hardcoded).
Virtual environment (venv) is set up and activated for all Python dependencies.
Recent Actions:

Successfully tested Slack notifications with error/suggestion messages.
Discussed Portia integration as the next major step.
Considered building a dashboard after Portia for user-friendly approval and monitoring.
Do’s for Next Session:

Activate your virtual environment:
Run your agent:
Check Slack for notifications.
For Portia integration:
Install Portia: pip install portia
Scaffold Portia agent to orchestrate workflow.
Refactor modules as Portia tools.
Next Steps:

Integrate Portia for agent orchestration and human-in-the-loop approval.
Optionally, build a dashboard for request visualization and approval after Portia.
Keep all secrets in .env and never commit them to GitHub.