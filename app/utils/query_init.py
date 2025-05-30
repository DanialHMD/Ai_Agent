class DatabaseHandler:
    def __init__(self, dialect, connection):
        self.dialect = dialect.lower()
        self.connection = connection

    def run_query(self, query):
        query = self.transform_query_for_dialect(query)
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                self.connection.commit()
                return "Query executed successfully."
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def transform_query_for_dialect(self, query):
        if self.dialect == "sqlite":
            return query.replace("%s", "?")  # For parameterized queries
        elif self.dialect == "postgresql":
            return query  # PostgreSQL already uses %s
        elif self.dialect == "mysql":
            return query.replace("AUTOINCREMENT", "AUTO_INCREMENT")
        else:
            raise ValueError(f"Unsupported SQL dialect: {self.dialect}")
