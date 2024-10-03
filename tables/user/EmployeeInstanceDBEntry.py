from base.DatabaseDriver import *
from tables import AccountInstance
from tables.user.PersonalInfoInstance import PersonalInfoInstance


# customer will have some redundancy.

class EmployeeInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the customer table.

    Will be added into the database upon init
    """

    __tablename__ = "Employee"

    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)
    account_id = Column(Integer, ForeignKey("Account.id"), nullable=True)
    account = relationship("AccountInstanceDBEntry", foreign_keys = [account_id])
    personal_info_id = Column(Integer, ForeignKey("PersonalInfo.id"))
    personal_info = relationship("PersonalInfoInstanceDBEntry", foreign_keys = [personal_info_id])
    # shopping_cart_id = Column(Integer, ForeignKey("ShoppingCart.id"))
    # shopping_cart = relationship('ShoppingCartInstanceDBEntry', foreign_keys = [shopping_cart_id])



    def __init__(self, personalInfo: PersonalInfoInstance, accountInstance:AccountInstance | None = None):
        # NOTE: personal info need not to be stored in the database..? or maybe so... as a record.
        # We should't be dynamically updating personal info then because we want to treat it like a snapshot.
        # Then maybe we should do a blob... but that may be out of scope.
        self.personalInfo = personalInfo
        self.accountInfo = accountInstance
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)
        # if accountInstance:
