from src.base_model import BaseModel


class User(BaseModel):
    _tableName = 'users'
    _primary_key = 'id'

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
