import sqlite3
import psycopg2
import mysql.connector

# def get_connection(dialect: QueryRequest):
#     if dialect == "sqlite":
#         return sqlite3.connect("my.db")
#     elif dialect == "postgresql":
#         return psycopg2.connect(
#             dbname="mydb", user="postgres", password="pass", host="localhost", port=5432
#         )
#     elif dialect == "mysql":
#         return mysql.connector.connect(
#             host="localhost", user="root", password="pass", database="mydb"
#         )
#     else:
#         raise ValueError("Unsupported dialect")

class DatabaseHandler:
    def __init__(self, dialect: str, connection=None) -> None:
        self.dialect = dialect.lower()
        self.connection = connection or self.get_connection()

    def run_query(self, query:str):
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

    def transform_query_for_dialect(self, query: str) -> str:
        if self.dialect == "sqlite":
            return query.replace("%s", "?")  # For parameterized queries
        elif self.dialect == "postgresql":
            return query  # PostgreSQL already uses %s
        elif self.dialect == "mysql":
            return query.replace("AUTOINCREMENT", "AUTO_INCREMENT")
        else:
            raise ValueError(f"Unsupported SQL dialect: {self.dialect}")
