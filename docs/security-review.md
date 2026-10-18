# SecureShop Security Review

## Intended controls

- Request validation and body-size limit
- Automated unit tests
- Bandit and Semgrep static analysis
- pip-audit dependency checking
- Gitleaks secret scanning
- Non-root Docker execution
- Trivy container image scanning
- OWASP ZAP baseline scan
- SBOM generation
- GitHub Actions CI

## Review requirements

1. Investigate all scanner findings.
2. Fix confirmed issues and rerun relevant checks.
3. Document false positives with a clear technical reason.
4. Do not commit secrets or sensitive scan artifacts.
5. Review workflow permissions and third-party actions.
6. Configure branch protection before relying on checks to block merges.
7. Define an explicit DAST alert policy before calling it a blocking gate.

## Verification status

Record actual results from the local environment and GitHub Actions.
The presence of a scanner configuration does not prove that a scan passed.

## Production gaps

The sample app lacks authentication, authorisation, rate limiting,
centralised logs, production monitoring and a formal release process.
