# Security Finding Remediation Playbook

1. Identify the scanner, rule, file, line or affected package.
2. Read the finding and supporting evidence.
3. Determine the affected component and realistic impact.
4. Prioritise based on severity, exploitability, exposure and fix availability.
5. Make the smallest safe change that addresses the root cause.
6. Rerun unit tests and the relevant security scan.
7. Confirm that expected application behaviour still works.
8. Record the finding, change, test evidence and remaining risk.
9. If an exception is justified, document its owner, rationale and review date.

Never suppress a finding merely to make the pipeline green.

A scanner result is evidence to investigate, not proof on its own
that a vulnerability is exploitable or that a system is secure.
