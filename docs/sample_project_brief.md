# Sample Project Brief — ProjectPilot AI

> This is fictional demonstration content created for testing File Search. It is not an official college policy or a record of real student work.

## Problem
Student teams often begin software projects with broad ideas but no clear problem statement, MVP scope, milestone plan, evaluation criteria, or risk register. This leads to unclear responsibilities and last-minute integration problems.

## Proposed solution
ProjectPilot AI is an agentic planning assistant backed by Microsoft Foundry. It accepts a project idea, creates a structured project plan, answers questions from approved uploaded documents, uses tools for data analysis, and can consult Microsoft Learn documentation through an MCP integration when configured.

## Core use cases
1. Convert a rough project idea into an MVP plan and implementation milestones.
2. Explain architecture choices and identify key risks.
3. Answer questions grounded in attached project documentation.
4. Analyze a synthetic project metrics CSV and summarize delayed/high-risk items.
5. Consult current official Microsoft documentation via an approved MCP tool when that tool is available.

## Non-goals
- Automatically submitting work to a college portal.
- Claiming team contributions that did not occur.
- Using confidential college/student data.
- Performing irreversible cloud operations without explicit human approval.

## Proposed architecture
Streamlit user interface → Python client → Microsoft Foundry project/agent → configured tools (File Search, Code Interpreter, and optional MCP server) → response returned to the user.

## Evaluation ideas
- Test whether generated project plans include all required sections.
- Verify document-grounded answers against the source document.
- Verify CSV metrics against independently calculated values.
- Confirm MCP references link to official Microsoft Learn pages.
- Test adversarial or off-topic prompts against the configured guardrails.
