from base.DatabaseDriver import *
from tables.PurchaseRecordInstance import PurchaseRecordInstance

"""
NOTICE

PERSONAL INFO TABLES IN THE DATABASE WILL ONLY CORRELATE TO USERS!!
NOT GUESTS
"""


class PurchaseRecordInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the teacher table.

    Will be added into the database upon init
    """

    __tablename__ = "PurchaseRecord"

    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("ProductInstanceDBEntry", foreign_keys = [product_id])
    name = Column(db.String(512), default = '')

    def __init__(self, purchaseRecord: PurchaseRecordInstance):
        self.name = purchaseRecord.product.name
        self.product_id = purchaseRecord.product.id
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)
