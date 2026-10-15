# ProjectPilot AI — Start Here

This package is a Phase I project starter for the college's Agentic AI and Data Engineering skill-based training. It is designed around the seven Microsoft learning links supplied by the student.

## What is ready now

- Streamlit UI source code, including a clearly labeled offline demo mode.
- A Microsoft Foundry agent connection path using Entra/Azure CLI authentication.
- Agent instructions for planning, document-grounded answers, data analysis, and optional Microsoft Learn MCP access.
- Synthetic project-metrics CSV and fictional sample project brief.
- Setup checks and a data-validation test.
- Editable Phase I report draft and presentation draft in `artifacts/`.
- A Cursor prompt and checklist.

## What is not done yet

No Azure resource or Foundry agent has been created from this package; no real Foundry request, model evaluation, MCP invocation, public hosting, or GitHub push has been performed. Those operations require access to your college-approved Azure subscription, the exact available models/permissions, and your team's GitHub account. The report and slides mark live checks as pending rather than fabricating evidence.

## Run the UI locally on macOS

Use Python 3.13 to match the Microsoft labs where possible.

```bash
cd projectpilot_ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

The default `DEMO_MODE=true` shows an offline preview only. It does not call an AI model. The sidebar explicitly labels this. Leave demo mode enabled until you have configured and tested a Foundry agent.

## Then follow this order

1. Open `docs/COLLEGE_LAB_MAPPING.md` and follow the assigned labs in sequence.
2. Create a Foundry project, deploy an available model, and record the real project endpoint and model deployment name.
3. Build and test the Foundry agent; configure only the tools that are actually available and required.
4. Copy the exact project endpoint and the agent's exact name into `.env`; run `az login` and set `DEMO_MODE=false` only after successful Foundry testing.
5. Verify tool invocations and numeric results in real traces; save genuine screenshots.
6. Run `pytest -q`, then create a GitHub repository under the approved team account and push the code without `.env`.
7. Replace all report/deck placeholders with the real team details and evidence before submission.

## Safety and cost

Do not paste Azure keys/tokens into chat, commit `.env`, or upload real student/college records without authorization. Model deployments and cloud resources may incur charges. Check the student subscription/credits and remove only resources that you own and are allowed to delete.
