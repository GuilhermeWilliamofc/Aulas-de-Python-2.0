from src.model.settings.db_metadata import metadados
from sqlalchemy import Table, Column, Integer, String

pessoa = Table(
    "pessoas",
    metadados,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)
