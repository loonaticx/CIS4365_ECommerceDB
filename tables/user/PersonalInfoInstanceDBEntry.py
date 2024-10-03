from base.DatabaseDriver import *
from tables.user.PersonalInfoInstance import PersonalInfoInstance

"""
NOTICE

PERSONAL INFO TABLES IN THE DATABASE WILL ONLY CORRELATE TO USERS!!
NOT GUESTS
"""

class PersonalInfoInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the teacher table.

    Will be added into the database upon init
    """

    __tablename__ = "PersonalInfo"

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)


    def __init__(self, piInstance:PersonalInfoInstance):
        self.first_name = piInstance.first_name
        self.last_name = piInstance.last_name
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)
