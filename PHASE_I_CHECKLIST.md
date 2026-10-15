# Phase I completion checklist

Use this before sending the GitHub URL, report, or presentation to the college.

## Microsoft Foundry
- [ ] Foundry project exists in the college-approved Azure subscription.
- [ ] A model deployment exists and its exact name/region are recorded.
- [ ] Agent is created; exact agent name is recorded.
- [ ] Agent instructions are saved.
- [ ] File Search is configured and the test document has indexed successfully.
- [ ] Code Interpreter has access to the synthetic CSV and numeric results were checked.
- [ ] MCP integration follows Lab 7, and the official Microsoft Learn MCP call is verified (only claim this if it actually ran).
- [ ] Content filters/guardrails are applied and test outcomes recorded.
- [ ] Model evaluation run is completed if required/available; actual metrics are recorded.

## Application
- [ ] Offline demo mode works and is labelled as a demo.
- [ ] `.env` contains the actual project endpoint and agent name; `.env` is not committed.
- [ ] `az login` succeeds with the intended student account.
- [ ] `DEMO_MODE=false` reaches the actual Foundry agent.
- [ ] Tool use and responses are verified in Foundry traces.
- [ ] App limitations and failure cases are tested.
- [ ] Public deployment (if requested) has an approved identity/authentication setup; no local Azure CLI login is assumed to work on the cloud host.

## GitHub and genuine teamwork
- [ ] Repository exists under the team/approved GitHub account.
- [ ] README lists setup steps, tools, architecture and limitations.
- [ ] `.env`, keys and credentials are not tracked.
- [ ] Each team member's role is agreed and accurate.
- [ ] Branches/commits/pull requests/reviews reflect actual work.
- [ ] GitHub URL opens and repository permissions are correct.

## Report and presentation
- [ ] Replace bracketed placeholders with real project/team information.
- [ ] Add screenshots captured from your own Azure/Foundry run.
- [ ] Replace evaluation placeholders with measured results or explicitly state that evaluation is pending.
- [ ] Explain what was completed, what was tested, and what remains.
- [ ] Confirm the format/report template with the faculty/instructor.
- [ ] Do not include student roll numbers or emails unnecessarily in a public repository.
