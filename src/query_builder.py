class QueryBuilder:
    def __init__(self):
        self._query = ""
        self._params = []

    def select(self, columns=None):
        params = ', '.join(columns) if columns else '*'
        self._query = f"SELECT {params}"
        return self

    def from_table(self, table):
        self._query += f" FROM {table}"
        return self

    def where(self, condition, param):
        self._query += f" WHERE {condition}"
        self._params.append(param)
        return self

    def insert_into(self, table, columns):
        self._query = f"INSERT INTO {table} ({', '.join(columns)})"
        return self

    def values(self, values):
        self._query += f" VALUES ({', '.join(['?'] * len(values))})"
        self._params.extend(values)
        return self

    def update(self, table):
        self._query = f"UPDATE {table}"
        return self

    def set(self, assignments):
        self._query += f" SET {', '.join(assignments)}"
        return self

    def delete_from(self, table):
        self._query = f"DELETE FROM {table}"
        return self

    def last_insert_id(self, primary_key, table):
        self._query = f"SELECT MAX({primary_key}) FROM {table}"
        return self

    def build(self):
        return self._query, self._params
