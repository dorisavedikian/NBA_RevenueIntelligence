import pandas as pd

from src.config import (
    EXECUTIVE_KPIS_PATH,
    EXECUTIVE_RECOMMENDATIONS_PATH,
    GAME_SEGMENTS_PATH,
    MODEL_DATASET_PATH,
    REVENUE_FORECASTS_PATH,
)


def test_analytics_outputs_exist():
    paths = [
        MODEL_DATASET_PATH,
        GAME_SEGMENTS_PATH,
        REVENUE_FORECASTS_PATH,
        EXECUTIVE_KPIS_PATH,
        EXECUTIVE_RECOMMENDATIONS_PATH,
    ]

    for path in paths:
        assert path.exists(), f"Missing output: {path}"


def test_model_dataset_not_empty():
    df = pd.read_csv(MODEL_DATASET_PATH)
    assert not df.empty
    assert "game_id" in df.columns
    assert "total_revenue" in df.columns
    assert "sell_through_rate" in df.columns


def test_sell_through_rate_valid():
    df = pd.read_csv(MODEL_DATASET_PATH)
    assert df["sell_through_rate"].between(0, 1).all()


def test_game_segments_exist():
    df = pd.read_csv(GAME_SEGMENTS_PATH)
    assert not df.empty
    assert "segment_name" in df.columns
    assert "business_recommendation" in df.columns


def test_revenue_forecasts_exist():
    df = pd.read_csv(REVENUE_FORECASTS_PATH)
    assert not df.empty
    assert "predicted_revenue" in df.columns
    assert "sellout_probability" in df.columns


def test_executive_recommendations_exist():
    df = pd.read_csv(EXECUTIVE_RECOMMENDATIONS_PATH)
    assert not df.empty
    assert "recommendation" in df.columns
    assert "priority" in df.columns


def test_executive_kpis_exist():
    df = pd.read_csv(EXECUTIVE_KPIS_PATH)
    assert not df.empty
    assert "total_revenue" in df.columns
    assert "total_tickets_sold" in df.columns
