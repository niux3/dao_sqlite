class BaseModel:
    _tableName = ''
    _primary_key = ''

    def __repr__(self):
        return f"<{self.__class__.__name__} {self._primary_key}={getattr(self, self._primary_key)}>"

