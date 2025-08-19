# Oncall AI Agent — Project Summary for GitHub Copilot

## **Project Goal**
Build an Oncall AI Agent powered by Portia that reads logs, diagnoses issues, and suggests solutions, so engineers on night shifts aren’t disturbed unnecessarily. The agent automates triage, notifies engineers via Slack, and only acts with human approval—focusing on safety, impact, and real-world use.

## **Key Decisions & Constraints**

- **Zero cost:** All tools and platforms used must be free and open-source.
- **Portia as core framework:** Use Portia for controllable agent planning, tool integration (Slack, log source), and human-in-the-loop approvals.
- **Sample log source:** Begin with local/sample log files in the repo; later, show how to integrate with real logs.
- **Simple diagnostics:** Start with regex/keyword matching for error detection, not paid ML models.
- **Slack for notifications:** Use Slack’s free tier for alerting engineers.
- **Human approval:** Never automate fixes without explicit engineer consent.
- **Modular architecture:** Separate log reading, error parsing, suggestion logic, notification, and approval for maintainability.
- **Auditability:** Log all agent actions and decisions for compliance and debugging.

## **Core Architecture (Diagram)**

```mermaid
flowchart TD
    A[Log Source<br>(local file)] --> B(Portia Agent)
    B --> C[Error Parser/Matcher<br>(regex, keywords)]
    C --> D[Suggestion Generator<br>(solution logic)]
    D --> E[Notification<br>(Slack API)]
    E --> F[Engineer (Human)]
    F -->|Approve| G[Portia Agent<br>(executes fix)]
    B --> H[Audit/Logs/Reporting]
    F -->|Decline| H
```

### **Component Breakdown**
- **Log Source:** Reads from local/sample files for simulation.
- **Portia Agent:** Orchestrates workflow, planning, and approval.
- **Error Parser:** Detects known patterns (regex/keywords).
- **Suggestion Generator:** Maps errors to recommended fixes.
- **Notification:** Sends actionable messages to Slack.
- **Human-in-the-loop:** Engineers approve/decline actions.
- **Audit/Logs:** Every suggestion and action is logged.

## **Best Practices**
- Keep each module independent for testability and future extension.
- Use environment variables for secrets—never hardcode credentials.
- Document everything: setup, architecture, safety logic, extensibility.
- Start with MVP (minimal features, clear flow), then iterate.
- Always prioritize safety and oversight over full automation.

## **Next Steps**
1. Create a sample log file in the repo.
2. Implement log reading and error detection (regex).
3. Build the Portia agent workflow: read logs → detect error → suggest fix → notify via Slack → ask for approval → execute or escalate.
4. Document how to swap to real log sources and add new error patterns.
5. Test end to end and ensure logging of all actions.

---

**This summary should guide Copilot and anyone collaborating on the repo.  
If anything changes, update this file and your README accordingly.**