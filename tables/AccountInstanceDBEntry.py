from sqlalchemy.orm import Mapped, mapped_column

from base.DatabaseDriver import *

from tables.AccountInstance import AccountInstance

# https://stackoverflow.com/questions/37908767/table-roles-users-is-already-defined-for-this-metadata-instance
class AccountInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the facility table.

    Will be added into the database upon init
    """

    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key = True)
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)
    username = Column(String(64))
    email = Column(String(128))
    pass_hash = Column(String(128))
    registered_on = Column(String(128))
    last_login = Column(String(128))


    def __init__(self, accountInstance: AccountInstance):
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)

        self.username = accountInstance.username
        self.email = accountInstance.email
        self.pass_hash = accountInstance.pass_hash
        self.registered_on = accountInstance.registered_on
        self.last_login = accountInstance.last_login


    def __repr__(self):
        return "<AccountInstanceDBEntry(username='%s')>" % (
            self.username,
        )


if __name__ == "__main__":
    pass
    # from base.DatabaseManager import *
    # from config.Config import Config
    # testDB = DatabaseManager(Config)
    # testDB.initSession()
    # testAccount = AccountInstance(
    #     username = "test",
    #     email = "",
    #     pass_hash = "",
    #     registered_on = "",
    #     last_login = ""
    # )
    # testAccountDB = AccountInstanceDBEntry(testAccount)
    # Database.generateEntry(testAccountDB)
    # print(testAccountDB)
