# Local validation record

Validation performed while preparing this starter package:

- `python -m py_compile app.py scripts/check_setup.py` — passed.
- `python -m pytest -q` — 1 test passed; the test validates the sample CSV schema and completion percentage range.
- The sample CSV and agent-instruction files exist.
- No `.env` file or Azure credential is included in the package.

Limitations of this validation:

- Streamlit is not installed in the authoring runtime, so the web UI was not launched here. Install `requirements.txt` and run `streamlit run app.py` to launch it locally.
- No Azure login, Foundry project, model deployment, agent, real API call, MCP invocation, content-filter test, model evaluation, public deployment, or GitHub remote was performed.
- The report and presentation are explicitly drafts. Complete their placeholders and add your own screenshots and measured results before submission.
