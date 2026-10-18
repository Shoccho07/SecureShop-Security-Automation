# SecureShop
## End-to-End DevSecOps Pipeline with Automated Security Gates

SecureShop is a DevSecOps portfolio project that demonstrates automated
security checks for a sample Python web application.

## Features

- Flask application with input validation
- pytest unit tests
- Bandit and Semgrep static analysis
- pip-audit dependency vulnerability checks
- Gitleaks secret scanning
- Docker image with non-root execution
- Trivy container vulnerability scanning
- OWASP ZAP baseline scan
- Syft SBOM generation
- GitHub Actions CI
- Security architecture, threat model and remediation documentation

## Architecture

Code change
-> tests and SAST/SCA/secret scanning
-> Docker build and image scan
-> SBOM generation
-> DAST baseline scan
-> investigate, remediate and rerun

## Local setup

    cd ~/Projects/SecureShop
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt -r requirements-dev.txt

## Unit tests

    python -m pytest -q

## Application security checks

    python -m bandit -r app
    semgrep scan --config p/python app
    python -m pip_audit -r requirements.txt

## Secret scanning

    gitleaks dir .

## Docker

    docker build -t secureshop:local .
    docker run --rm -d --name secureshop-local \
      -p 127.0.0.1:5000:5000 secureshop:local

    curl -i http://127.0.0.1:5000/health

Stop the container:

    docker stop secureshop-local

## Container scan and SBOM

    trivy image --severity HIGH,CRITICAL secureshop:local
    syft secureshop:local -o cyclonedx-json=reports/secureshop-sbom.json

Create the reports directory before generating the SBOM:

    mkdir -p reports

## DAST

Run OWASP ZAP baseline scanning only against the local application or
another target for which you have explicit permission.

## GitHub Actions

The workflow runs automated tests and security checks on pushes and
pull requests. Review the actual job results in the repository's Actions tab.

## Security boundaries

- This is a learning application, not a production shopping service.
- No AWS resources are deployed.
- Do not commit secrets, credentials or private keys.
- Investigate findings rather than suppressing them to obtain a green run.
- A clean scan does not prove the absence of vulnerabilities.
- ZAP baseline scanning is not a full penetration test.
- Review and pin third-party GitHub Actions before production use.

## Validation evidence

Record actual test, scanner, Docker and CI results here after running them.
Do not claim that checks passed before inspecting their output.
