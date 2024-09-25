import sqlite3
from src.configuration import Configuration

class DatabaseConnection:
    def __init__(self):
        self._db_path = Configuration.DNS.value
        self._connection = None

    def __enter__(self):
        self._connection = sqlite3.connect(self._db_path)
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection:
            self._connection.close()
