# Config

## Configuration & Environment Variables

All secrets and configuration should be set via environment variables or config files. Never hardcode credentials.

### Required/Optional Environment Variables
- `ONCALL_LOG_PATH`: Path to the log file to process (default: `sample_logs/single_error.log`)
- `ONCALL_SLACK_TOKEN`: Slack API token for notifications (required for real Slack integration)
- `ONCALL_AUDIT_LOG_PATH`: Path to the audit log file (default: `audit.log`)

### Usage
Import config variables from `config/config.py` in your modules:

```python
from config.config import LOG_PATH, SLACK_TOKEN, AUDIT_LOG_PATH
```

Update this file when adding new configuration options.
