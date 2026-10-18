# SecureShop Architecture

## Purpose

SecureShop demonstrates an automated DevSecOps pipeline for a sample
Python web application. It does not represent a complete online store.

## Components

- Flask: sample web application.
- pytest: application behaviour tests.
- Bandit and Semgrep: static code analysis.
- pip-audit: Python dependency vulnerability audit.
- Gitleaks: potential secret detection.
- Docker: container image build.
- Trivy: container vulnerability scanning.
- OWASP ZAP: baseline testing of the running local application.
- Syft: software bill of materials generation.
- GitHub Actions: automated CI workflow.

## Pipeline

Code change
-> unit tests and application scans
-> container build and image scan
-> SBOM artifact
-> running application baseline scan
-> review findings and remediate

## Scope and limitations

This project does not deploy AWS resources. The sample application does
not implement production authentication, authorisation, rate limiting,
payment processing or centralised monitoring.
