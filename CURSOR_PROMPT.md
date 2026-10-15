# Optional Cursor prompt

Open the `projectpilot-ai-foundry` repository in Cursor and paste this prompt. Cursor is an optional coding assistant; your college's Microsoft labs use Visual Studio Code.

---

You are helping me improve an existing student project called **ProjectPilot AI**, a Streamlit user interface that calls a Microsoft Foundry agent. Read `README.md`, `app.py`, `.env.example`, `docs/agent_instructions.md`, and the tests before editing anything.

Requirements:
1. Preserve the distinction between offline demo mode and a real Microsoft Foundry request. Never label a demo answer as live AI.
2. Keep credentials out of source files. Never print API keys, tokens, `.env` content, or user secrets. Do not commit `.env`.
3. Keep the existing official Microsoft Foundry SDK integration and use the current documented API. If API behavior is uncertain, tell me what must be checked against Microsoft Learn instead of inventing methods.
4. Improve accessibility, responsive layout, input validation, error handling, and test coverage.
5. Do not add fake screenshots, fake benchmark scores, fabricated team contributions, or a claim that the Azure service was tested unless we actually run it.
6. Do not silently replace Streamlit with Google tooling. Do not deploy or create paid cloud resources without asking me first.
7. Before finishing, explain each changed file, run the tests you can run locally, and list what still requires Azure credentials or a real Foundry agent.

First inspect the code and propose a small implementation plan. Then make changes in manageable steps.
