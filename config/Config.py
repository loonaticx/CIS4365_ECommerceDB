from dataclasses import dataclass

from base.ConnectionType import ConnectionType


@dataclass
class Config:
    REMOTE_USERNAME: str = "admin"
    REMOTE_PASSWORD: str = "a"
    REMOTE_HOST: str = "dd"
    SCHEMA: str = "DaycareDatabase"

    # Will output active transactions being made to the database in console
    VERBOSE_OUTPUT: bool = True
    
    UUID_TOKEN_LENGTH: int = 32

    # LOCAL_FILE, LOCAL_MEMORY, REMOTE_SERVER
    CONNECTION_MODE: ConnectionType = ConnectionType.LOCAL_FILE

    LOCAL_FILENAME: str = "data.db"

    FLASK_HOST = "localhost"
    FLASK_WANT_DEBUG = False
    FLASK_OVERRIDE_AUTH = True
