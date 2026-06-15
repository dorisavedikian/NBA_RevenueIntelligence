import sqlite3

from src.config import DATABASE_PATH


def test_database_exists():
    assert DATABASE_PATH.exists()


def test_required_tables_exist():
    required_tables = {
        "dim_games",
        "dim_customers",
        "dim_sections",
        "dim_promotions",
        "fact_ticket_transactions",
        "fact_web_sessions",
        "model_dataset",
        "game_segments",
        "revenue_forecasts",
        "executive_kpis",
        "executive_recommendations",
    }

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'view')")
        existing = {row[0] for row in cursor.fetchall()}

    missing = required_tables - existing
    assert not missing, f"Missing tables/views: {missing}"
