from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_sample_data_has_required_columns_and_valid_percentages():
    data = pd.read_csv(ROOT / "sample_data" / "project_metrics.csv")
    required = {"work_item", "completion_percent", "status", "risk_level"}
    assert required.issubset(data.columns)
    assert len(data) >= 1
    assert data["completion_percent"].between(0, 100).all()
    assert data["work_item"].notna().all()
