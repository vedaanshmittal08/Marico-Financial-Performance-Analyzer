import pytest
import project

def test_load_data():
    df = project.load_data()

    assert not df.empty
    assert len(df) == 4
    assert "revenue_from_operations" in df.columns

def test_calculate_metrics():
    df = project.calculate_metrics(project.load_data())

    assert "ebitda" in df.columns
    assert "nopat" in df.columns
    assert "fcff" in df.columns

    assert df.iloc[-1]["operating_nwc"] == pytest.approx(1281)
    assert df.iloc[-1]["change_in_nwc"] == pytest.approx(81)
    assert df.iloc[-1]["fcff"] == pytest.approx(1494.77)

def test_summarize_performance():
    df = project.calculate_metrics(project.load_data())

    summary = project.summarize_performance(df)

    assert summary["Revenue CAGR"] == pytest.approx(0.1134, abs=0.0001)
    assert summary["EBITDA CAGR"] == pytest.approx(0.0875, abs=0.0001)
    assert summary["Latest EBITDA Margin"] == pytest.approx(0.1727, abs=0.0001)
