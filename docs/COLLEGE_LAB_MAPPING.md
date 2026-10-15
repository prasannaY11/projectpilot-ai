# College Microsoft Agentic AI lab mapping

This guide maps the seven links supplied for the SNIST Skill-Based Training Program to ProjectPilot AI. The linked materials are learning exercises; they do not themselves prove that a combined application has been completed.

## Recommended project concept

**ProjectPilot AI — Agentic Project Planning and Data Insights Assistant.** A student-facing assistant that turns project ideas into an implementation plan, answers questions from an approved project brief, analyzes synthetic project metrics, and looks up official Microsoft technical documentation through an MCP tool when configured.

## Link-to-project mapping

| # | Official exercise/module | How to use it in this project | Evidence to capture after your own run |
|---|---|---|---|
| 1 | [Prepare for an AI development project](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/01-Explore-ai-studio.html) | Create the Foundry project, select/deploy a permitted model, inspect the project endpoint and connect VS Code to the project. | Project overview (with secrets hidden), chosen region, deployment name, VS Code Foundry Toolkit connection. |
| 2 | [Explore and compare models](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/02-model-catalog-evaluation.html) | Compare model cards/benchmarks and, where available and affordable, run the supplied evaluation exercise. Record actual results instead of assuming the preferred model. | Model comparison observations, evaluation configuration, run results and failure analysis. |
| 3 | [Create a generative AI app that uses tools](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/04a-use-own-data.html) | Learn to use web search and file search from a Responses API application. Apply the pattern to approved project documents and trusted current references as supported by the chosen app/agent configuration. | A grounded answer from the uploaded brief and a response where web search is actually invoked. |
| 4 | [Apply guardrails to prevent harmful content](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/06-Explore-content-filters.html) | Configure and test the available content-filter/guardrail options for the project. | Actual allow/block tests and the configured policy. Do not claim that a safety filter was applied unless it was. |
| 5 | [Build AI agents with portal and VS Code](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/01-build-agent-portal-and-vscode.html) | Create the agent, add grounding data and built-in tools, then invoke the agent programmatically. ProjectPilot's fictional brief and synthetic CSV can serve as project-specific test inputs. | Agent name/version, File Search result, Code Interpreter analysis, invocation from VS Code. |
| 6 | [Develop AI agents in Azure with VS Code](https://learn.microsoft.com/en-us/training/modules/develop-ai-agents-azure-vs-code/1-introduction?pivots=text) | Complete the learning module and record any required knowledge checks/achievement in the manner specified by the instructor. | Training completion/achievement evidence if required by the program. |
| 7 | [Extend agents with Model Context Protocol tools](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/03-mcp-integration.html) | Follow the provided code exercise to connect to the Microsoft Learn remote MCP server. The exercise's example uses an approval flow. Integrate MCP into the project only after a real call works. | Agent trace showing an MCP tool call and a response sourced from official Microsoft Learn documentation. |

## Project features and how they map

- **Project planning:** agent instructions structure a solution into a problem, users, MVP, architecture, milestones, risks, and evaluation.
- **Grounded Q&A:** upload `sample_project_brief.md` to the configured File Search tool and ask questions answered by that file.
- **Data engineering:** use `sample_data/project_metrics.csv` as synthetic input; validate schema/ranges and compare agent calculations with independent calculations.
- **Reference retrieval:** configure the Microsoft Learn MCP server as described in lab 7 and approve tool calls according to the configured policy.
- **Safety:** configure content filters according to lab 4 and record actual behavior.
- **Evaluation:** use lab 2's evaluation workflow if the permitted deployment and subscription support it; record measured scores and failures.
- **Web UI:** `app.py` is a Streamlit client. In demo mode it returns local sample responses; in live mode it invokes a pre-created Foundry agent. The app does not create Azure resources or configure tools by itself.

## Important integration note

Some of these labs create separate sample agents or applications. For example, the MCP lab creates an agent with an MCP tool, while the portal/VS Code agent exercise demonstrates grounding and Code Interpreter. Do not assume those tools automatically coexist in one agent. Configure the desired tools on your own project's agent (or combine the documented code patterns), then verify each tool invocation in the actual trace.

## Submission evidence checklist

- [ ] Team topic and team number approved by the instructor.
- [ ] Foundry project and model details recorded from the real environment.
- [ ] File Search and Code Interpreter tested with project files.
- [ ] Content filter behavior tested and recorded.
- [ ] MCP call actually completed, if used.
- [ ] Evaluation run and observed outputs captured where required.
- [ ] Local UI shown in both demo mode (optional) and live mode; label screenshots accurately.
- [ ] `pytest -q` output captured.
- [ ] GitHub repository created and `.env` excluded.
- [ ] Report and presentation updated with real screenshots, team details, measured results, and limitations.
