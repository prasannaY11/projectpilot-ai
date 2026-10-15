"""Check local configuration without making a model call or printing credentials."""
from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

checks = {
    ".env exists": (ROOT / ".env").exists(),
    "FOUNDRY_PROJECT_ENDPOINT set": bool(os.getenv("FOUNDRY_PROJECT_ENDPOINT", "").strip()),
    "FOUNDRY_AGENT_NAME set": bool(os.getenv("FOUNDRY_AGENT_NAME", "").strip()),
    "sample CSV exists": (ROOT / "sample_data" / "project_metrics.csv").exists(),
    "agent instructions exist": (ROOT / "docs" / "agent_instructions.md").exists(),
}
for label, ok in checks.items():
    print(f"{'[OK]' if ok else '[MISSING]'} {label}")
print("\nThis script does not test Azure permissions, endpoint reachability, quotas, or the agent itself.")
if not all(checks.values()):
    raise SystemExit(1)
