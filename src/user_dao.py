from src.model import User
from src.base_dao import BaseDAO


class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__(User)

    def create_user(self, name, email):
        return self.create(name=name, email=email)

    def get_user(self, id):
        return self.get(id)

    def update_user(self, id, name=None, email=None):
        updates = {k: v for k, v in {'name': name, 'email': email}.items() if v is not None}
        if updates:
            self.update(id, **updates)

    def delete_user(self, id):
        self.delete(id)

    def list_users(self):
        return self.list()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        """
        self._execute_query(query)
