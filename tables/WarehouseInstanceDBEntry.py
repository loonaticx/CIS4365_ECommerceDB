from sqlalchemy.orm import Mapped, mapped_column
from tables.WarehouseInstance import WarehouseInstance

from base.DatabaseDriver import *


class WarehouseInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the facility table.

    Will be added into the database upon init
    """

    __tablename__ = "Warehouse"

    id: Mapped[int] = mapped_column(primary_key = True)
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)
    name = Column(String(64))
    products = relationship("ProductInstanceDBEntry", back_populates = "Warehouse")

    def __init__(self, warehouseInstance: WarehouseInstance):
        self.name = warehouseInstance.name
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)

    def __repr__(self):
        return "<WarehouseInstanceDBEntry(name='%s')>" % (
            self.name,
        )
