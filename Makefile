.PHONY: test bandit semgrep audit secrets security docker-build image-scan

test:
	python -m pytest -q

bandit:
	python -m bandit -r app

semgrep:
	semgrep scan --config p/python app

audit:
	python -m pip_audit -r requirements.txt

secrets:
	gitleaks dir .

security:
	./scripts/run_security_checks.sh

docker-build:
	docker build -t secureshop:local .

image-scan:
	trivy image --severity HIGH,CRITICAL secureshop:local
