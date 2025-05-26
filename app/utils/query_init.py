import mysql.connector
import psycopg2
import sqlite3

class SQLQUERIES:
    def __init__(self):
        self.postgre_cursor = psycopg2.connect("dbname='none for now' user='username' host='localhost' password='password'").cursor()
        self.sqlite_cursor = sqlite3.connect(database="none for now").cursor()
        self.mysql_cursor = mysql.connector.connect(host="localhost", port=3306, user="username", password="password").cursor()

    def dialect_finder(self):
        pass

    def postgresql(self, query):
        self.postgre_cursor.execute(query)
    
    def sqlite(self, query):
        pass

    def mysql(self, query):
        pass

    def query_initiator(self, query):
        pass