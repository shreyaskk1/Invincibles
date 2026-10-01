# Invincibles QA360 Demo Project

This repository is a small Python project wired for QA360 telemetry.

When GitHub Actions runs, it publishes:

- project registration metadata
- user-wise `code_checkin` events from commit authors on pushes
- PR/MR metadata from pull request events
- `automation_report` from the generated JUnit XML report

QA360 computes total, passed, failed, skipped, error, and flaky tests from the execution report.

## Local Test

```powershell
python -m pip install -r requirements.txt
python -m pytest --junitxml qa360-junit.xml
```

## GitHub Setup

Create repository secret:

```text
QA360_BASE_URL=http://YOUR_QA360_HOST:5000
```

Optional repository secret:

```text
QA360_API_TOKEN=demo-token
```

Recommended repository variables:

```text
QA360_PROJECT_KEY=invincibles-new-project
QA360_PROJECT_NAME=Invincibles
QA360_CLIENT=Centric Hackathon
QA360_PORTFOLIO=QA Practice
QA360_INDUSTRY=consulting
QA360_CRITICALITY=Tier 1
QA360_RELEASE_TRAIN=QA360-DEMO
QA360_OWNER=Invincibles Team
QA360_QA_LEAD=Invincibles QA
QA360_REPO_TOOL=GitHub
QA360_CI_TOOL=GitHub Actions
QA360_UI_TOOL=Pytest
QA360_API_TOOL=Python Requests
QA360_DATA_TOOL=SQL Server
QA360_SECURITY_TOOL=GitHub Advanced Security
QA360_PERFORMANCE_TOOL=k6-ready
QA360_DEFECT_TOOL=GitHub Issues
```

If GitHub Actions is running in GitHub cloud, `127.0.0.1` will not reach your laptop. Use a self-hosted runner, LAN-accessible host, or tunnel URL.
