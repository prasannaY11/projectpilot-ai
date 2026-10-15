# ProjectPilot AI — Agentic Project Planning & Data Insights Assistant

> **Start here:** read [`START_HERE.md`](START_HERE.md) first, then follow [`docs/COLLEGE_LAB_MAPPING.md`](docs/COLLEGE_LAB_MAPPING.md) for the exact seven college-provided Microsoft learning links.

**Phase I starter project for the SNIST Skill-Based Training Program: Agentic AI and Data Engineering.**

ProjectPilot AI is a small web app that calls a Microsoft Foundry agent. The agent is intended to help student teams scope a project, explain architecture, answer questions from uploaded project documents, analyze structured project metrics, and consult official Microsoft documentation through an MCP tool when that tool is configured.

> **Current status:** The local Streamlit UI has been run with `DEMO_MODE=false` and configured Microsoft Foundry settings. Project-planning responses and the CSV memory-usage chart workflow were tested locally, including PNG download. The included automated test passes (`1 passed`). The GitHub repository is private, and the application has not been deployed to a public URL. Before claiming complete Foundry integration for assessment, verify the live agent and tool calls and capture evidence from your own run. The project report and presentation remain drafts, and team contributions must reflect work actually completed.

## Included

- `app.py` — Streamlit web interface; offline demo by default; can call a Foundry agent.
- `docs/agent_instructions.md` — copy/paste instructions for the agent.
- `docs/sample_project_brief.md` — fictional document to upload to File Search.
- `sample_data/project_metrics.csv` — synthetic data for Code Interpreter testing.
- `scripts/check_setup.py` — checks local configuration files without contacting Azure.
- `tests/test_demo_data.py` — simple data validation test.
- `.env.example` — safe configuration template.
- `CURSOR_PROMPT.md` — prompt for using Cursor as an optional coding assistant.
- `PHASE_I_CHECKLIST.md` — Azure, GitHub, testing, report and presentation checklist.

## Architecture

```text
Student
  │
  ▼
Streamlit web UI (app.py)
  │  Azure Entra ID via DefaultAzureCredential
  ▼
Microsoft Foundry project / named agent
  ├── File Search: attached project brief and approved documents
  ├── Code Interpreter: project_metrics.csv and data questions
  ├── MCP tool (optional): Microsoft Learn Docs MCP server
  └── Foundry guardrails/content filters
  │
  ▼
Grounded answer + actionable project guidance
```

The Streamlit app does not create the agent or attach tools. Configure those in Foundry/VS Code first. An MCP tool only works if the agent has actually been created/configured with MCP as taught in Lab 7.

## 1. Run the UI in offline demo mode

Requires Python 3.10+; the supplied Microsoft labs specifically recommend Python 3.13. The `azure-ai-projects` SDK also supports Python 3.10+ in recent releases.

```bash
# Run these commands from the project root directory
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# On Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

`DEMO_MODE=true` means the app displays a local, clearly labeled UI preview. It does not call an AI model. This lets you check the interface before configuring Azure.

## 2. Configure Microsoft Foundry

Use the official exercises your instructor supplied. Menu names can vary with the portal experience, available model deployments, region, and subscription permissions.

1. Open [Microsoft Foundry](https://ai.azure.com/) and sign in with the Azure account issued/approved by your college.
2. Create a project and deploy one model that your subscription can use. The linked labs name GPT-5.2 / GPT-5-mini; if the catalog, quota, or college subscription does not offer them, use a model approved by your instructor and record the difference in your report. Do not repeatedly deploy models just to experiment; deployment usage may incur Azure charges.
3. Create an agent named `projectpilot-agent` (or choose another name and use the exact same name in `.env`). Paste the instructions from `docs/agent_instructions.md`.
4. Add **File Search** and upload `docs/sample_project_brief.md`. Wait until indexing is complete, then test questions whose answers are in the brief.
5. Add **Code Interpreter** and attach `sample_data/project_metrics.csv` for data-analysis requests. Test the outputs against manually calculated values.
6. Configure the required content filters/guardrails using Lab 4. Record what you tested; don't claim a filter is configured unless you applied and verified it.
7. For MCP support, complete the supplied Lab 7 and configure the agent using the official Microsoft Learn MCP endpoint `https://learn.microsoft.com/api/mcp`, with approval settings as specified in the lab. The example lab creates/configures an agent in code; it is **not** enabled automatically by entering a prompt in the portal.
8. In Foundry, test the agent first. Confirm that File Search and Code Interpreter are invoked for appropriate queries, and that an MCP call runs only if MCP has been configured.

Official labs:
- [1 — Prepare for an AI development project](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/01-Explore-ai-studio.html)
- [2 — Explore and compare models](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/02-model-catalog-evaluation.html)
- [3 — Create a generative AI app that uses tools](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/04a-use-own-data.html)
- [4 — Apply guardrails/content filters](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/06-Explore-content-filters.html)
- [5 — Build AI agents with portal and VS Code](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/01-build-agent-portal-and-vscode.html)
- [6 — Develop AI agents in Azure with VS Code](https://learn.microsoft.com/en-us/training/modules/develop-ai-agents-azure-vs-code/1-introduction?pivots=text)
- [7 — Extend agents with MCP tools](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/03-mcp-integration.html)

**Important:** these are individual learning labs with different demo scenarios. Reuse their concepts, but do not assume their separate sample agents, starter code, or endpoints are one combined app.

## 3. Connect this UI to the real agent

1. Sign in to Azure from Terminal:

   ```bash
   az login
   az account show
   ```

2. Copy `.env.example` to `.env` if you have not already. Set:

   ```dotenv
   FOUNDRY_PROJECT_ENDPOINT=https://YOUR-RESOURCE.services.ai.azure.com/api/projects/YOUR-PROJECT
   FOUNDRY_AGENT_NAME=projectpilot-agent
   DEMO_MODE=false
   ```

   Use the **project endpoint**, not an API key and not a made-up URL. Copy the exact endpoint shown in your Foundry project. Use the exact registered agent name.

3. Check local configuration:

   ```bash
   python scripts/check_setup.py
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

5. Ask the agent a question, verify the output, and inspect the Foundry trace/tool activity. If the call fails, see Troubleshooting.

The integration in `app.py` follows the `agent_reference` call style shown in the supplied Microsoft agent exercise. SDK and agent endpoint modes can differ between Foundry experiences. If your lab is using a direct agent-scoped endpoint instead, follow the currently documented SDK pattern in [Microsoft's Foundry agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-agent-catalog) and adjust the client invocation to match that agent configuration.

## 4. What counts as a real demonstration

Demonstrate, rather than merely describe:

1. A real query in Foundry playground and the answer.
2. A File Search question whose answer is grounded in `sample_project_brief.md`.
3. A CSV analysis request whose numerical output is cross-checked independently.
4. An MCP request to Microsoft Learn, if MCP has been configured.
5. A content-filter/guardrail test with the outcome recorded.
6. The Streamlit UI connected to the real agent (not just offline demo mode).
7. A model evaluation run and its actual scores, where possible.

Capture screenshots from your own run. Never invent successful runs, benchmark results, or deployment URLs for the report.

## 5. GitHub repository and team workflow

The ProjectPilot AI source code is maintained in the [ProjectPilot AI GitHub repository](https://github.com/prasannaY11/projectpilot-ai), on the `main` branch. The repository is currently private, so users need repository access to clone it.

### Clone the repository

```bash
git clone https://github.com/prasannaY11/projectpilot-ai.git
cd projectpilot-ai
```

### Verify configuration safety

Before committing or pushing changes, confirm that local environment files are excluded:

```bash
git check-ignore -v .env .venv/
git status --short
```

Never commit `.env`, virtual environments, API keys, passwords, access tokens, or other secrets.

### Save and publish future changes

```bash
git add <files>
git commit -m "Describe your change"
git push
```

Replace `<files>` with the specific files you intend to commit.

### Team collaboration

For collaborative development, invite actual team members through the repository settings. Each contributor should work on a separate branch, open pull requests, review other contributions, and merge tested changes.

Ensure that the repository history, team contributions, screenshots, and project report accurately reflect the work that was actually completed.

## 6. Tests

Run the included data test:

```bash
pip install pytest
pytest -q
```

The test validates the sample dataset format. It does **not** test Foundry, Azure permissions, model quality, the MCP server, or the deployed website.

## Troubleshooting

- **401/403 or authorization error:** run `az login`, check `az account show`, verify the signed-in account and ensure it has the required Foundry/Azure role. Ask the resource owner/instructor to verify permissions.
- **Wrong endpoint:** copy the project endpoint exactly from the Foundry project. The endpoint format usually resembles `https://<resource>.services.ai.azure.com/api/projects/<project>`.
- **Agent not found:** `FOUNDRY_AGENT_NAME` must exactly match the name used when creating the agent; agent versions and endpoint mode must match the Microsoft lab you followed.
- **Model not available or quota exceeded:** choose a permitted model/region with the instructor or subscription administrator. Do not assume every model is available to all student subscriptions.
- **MCP not used:** the web UI does not add MCP by itself. Complete Lab 7 and verify MCP tool invocation in agent traces.
- **Cost:** model deployments and some Azure resources may incur charges. Check the Azure Cost Management/credits view, stop/delete unused deployments and resources according to college instructions, and do not delete shared college resources.
- **Demo looks successful but is not live:** when `DEMO_MODE=true`, all answers are local preview text. Set `DEMO_MODE=false` only after the agent is configured and sign-in works.

## References

1. Microsoft Learning, Prepare for an AI development project: https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/01-Explore-ai-studio.html
2. Microsoft Learning, Explore and compare models: https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/02-model-catalog-evaluation.html
3. Microsoft Learning, Create a generative AI app that uses tools: https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/04a-use-own-data.html
4. Microsoft Learning, Apply guardrails to prevent harmful content: https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/06-Explore-content-filters.html
5. Microsoft Learning, Build AI agents with portal and VS Code: https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/01-build-agent-portal-and-vscode.html
6. Microsoft Learn, Develop AI agents in Azure with VS Code: https://learn.microsoft.com/en-us/training/modules/develop-ai-agents-azure-vs-code/1-introduction?pivots=text
7. Microsoft Learning, Extend agents with Model Context Protocol tools: https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/03-mcp-integration.html
8. Microsoft Learn, Create a prompt agent: https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-agent-catalog
