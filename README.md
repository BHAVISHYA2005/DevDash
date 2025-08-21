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
