from app.utils.query_init import DatabaseHandler

def test_sqlite_query_execution():
    db = DatabaseHandler("sqlite")
    result = db.run_query("CREATE TABLE IF NOT EXISTS test (id INTEGER);")
    assert result == "Query executed successfully."
