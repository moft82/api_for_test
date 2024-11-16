import os
from app.core.config import Config
from alembic.config import Config as AlembicConfig
from alembic import command

class Migrator:
    def __init__(self):
        self.config = Config()
        self.alembic_config = AlembicConfig("alembic.ini")
        