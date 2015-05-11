#author: Ivan Rodriguez
import sqlite3


class LogDb():
    """ Simple helper to interface with sqlite."""

    def __init__(self, dbname="logs.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        self.conn.row_factory = sqlite3.Row
        self.conn.text_factory = str

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def create_table(self):
        """Create logs table."""
        cursor = self.cursor()
        cursor.execute("DROP TABLE IF EXISTS logs")
        cursor.execute("""
        CREATE TABLE logs (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           cc_number text,
           cc_type text,
           valid int

        )
        """)

    def clear_logs(self):
        """Clears the database"""
        cursor = self.cursor()
        cursor.execute("DELETE FROM logs")

    def add_log(self, number, type):
        """Adds a log to the database"""
        cursor = self.cursor()
        cursor.execute("INSERT INTO logs (cc_number, cc_type) VALUES (?, ?)", (number, type) )
        self.commit()
        return cursor.lastrowid
