from base.DatabaseDriver import *
from tables.ProductInstance import ProductInstance

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from typing import List



class ProductInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the teacher table.

    Will be added into the database upon init
    """

    __tablename__ = "Product"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(64))
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)

    product_warehouse = relationship(
        "WarehouseItemDBEntry",
        back_populates="child"
    )


    def __init__(self, productInstance: ProductInstance):
        self.name = productInstance.name
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)
