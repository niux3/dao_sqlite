import sqlite3
from src.db import DatabaseConnection
from src.query_builder import QueryBuilder


class BaseDAO:
    def __init__(self, entity):
        self._entity = entity
        self._table_name = entity._tableName
        self._primary_key = entity._primary_key

    def _get_last_inserted_id(self):
        query, params = QueryBuilder().last_insert_id(self._primary_key, self._table_name).build()
        row = self._execute_query(query, params, fetch_one=True)
        return row[0] if row else None

    def _get_column_names(self):
        query = f"PRAGMA table_info({self._table_name})"
        rows = self._execute_query(query, fetch_all=True)
        return [row[1] for row in rows]

    def create(self, **kwargs):
        query, params = QueryBuilder().insert_into(self._table_name, kwargs.keys()).values(kwargs.values()).build()
        self._execute_query(query, params)
        last_id = self._get_last_inserted_id()
        return last_id

    def get(self, id):
        query, params = QueryBuilder().select().from_table(self._table_name).where(f'{self._primary_key} = ?', id).build()
        row = self._execute_query(query, params, fetch_one=True)
        if row:
            columns = self._get_column_names()
            data = dict(zip(columns, row))
            return self._entity(**data)
        return None

    def update(self, id, **kwargs):
        set_clause = [f'{n} = ?' for n in kwargs.keys()]
        query, params = QueryBuilder().update(self._table_name).set(set_clause).where(f'{self._primary_key} = ?', id).build()
        self._execute_query(query, list(kwargs.values()) + params)

    def delete(self, id):
        query, params = QueryBuilder().delete_from(self._table_name).where(f'{self._primary_key} = ?', id).build()
        self._execute_query(query, params)

    def list(self):
        query, params = QueryBuilder().select().from_table(self._table_name).build()
        rows = self._execute_query(query, params, fetch_all=True)
        columns = self._get_column_names()
        return [self._entity(**dict(zip(columns, row))) for row in rows]

    def _execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                if fetch_one:
                    return cursor.fetchone()
                if fetch_all:
                    return cursor.fetchall()

                connection.commit()  # Commit des modifications
            except sqlite3.Error as e:
                connection.rollback()  # Annule la transaction en cas d'erreur
                print(f"Erreur lors de l'exécution de la requête : {e}")
                exit()
