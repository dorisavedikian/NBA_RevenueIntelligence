from src.config import (
    ANALYTICS_DIR,
    DATABASE_PATH,
    RAW_DIR,
    WAREHOUSE_DIR,
)


def test_config_directories_exist():
    assert RAW_DIR.exists()
    assert WAREHOUSE_DIR.exists()
    assert ANALYTICS_DIR.exists()


def test_database_path_points_to_warehouse():
    assert "warehouse" in str(DATABASE_PATH)
    assert DATABASE_PATH.name.endswith(".sqlite")
