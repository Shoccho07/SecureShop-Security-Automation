# SecureShop Threat Model

## Scope

The sample Flask application, Python dependencies, Docker image,
Git repository and CI workflow.

## Assets

- Application availability and integrity
- Dependency and build integrity
- Repository credentials and CI permissions
- Container image and SBOM
- Security scan evidence

## Threats and controls

### Invalid or oversized input

Threat:
Malformed or oversized requests can cause unexpected behaviour
or consume application resources.

Controls:
Validate content type, JSON structure, input type and length.
Limit request body size and test invalid inputs.

### Vulnerable dependencies

Threat:
A third-party package may contain a known vulnerability.

Controls:
Run pip-audit and review upgrade recommendations.

### Unsafe code patterns

Threat:
A code change may introduce a known risky programming pattern.

Controls:
Run Bandit and Semgrep and investigate their findings.

### Exposed secrets

Threat:
A developer may accidentally commit an API key or password.

Controls:
Run Gitleaks. Never commit real credentials.
Rotate a real secret immediately if it is exposed.

### Vulnerable container components

Threat:
The base image or an installed library may contain a known vulnerability.

Controls:
Scan the built image with Trivy and rebuild after remediation.

### Web application weaknesses

Threat:
A running application may expose security misconfigurations or
other detectable web security issues.

Controls:
Run an OWASP ZAP baseline scan against the local sample application.

### CI supply-chain risks

Threat:
A compromised third-party action or excessive workflow permission
could affect the build pipeline.

Controls:
Use minimum permissions, review action sources and pin verified
full commit SHAs before production use.

## Residual risks

- No production authentication or authorisation.
- No live penetration test.
- No production deployment or cloud security assessment.
- No guarantee that scanners identify every vulnerability.
- ZAP baseline scanning is not a full penetration test.
- The sample application is not suitable for real customer data.
