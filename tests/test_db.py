import pytest
from unittest.mock import patch, MagicMock
from src.db import DatabaseConnection
from src.configuration import Configuration

def test_database_connection():
    with patch('sqlite3.connect') as mock_connect:
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        with DatabaseConnection() as conn:
            assert conn is mock_connection
        mock_connect.assert_called_once_with(Configuration.DNS.value)
