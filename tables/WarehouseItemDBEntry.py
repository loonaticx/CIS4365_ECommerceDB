from tables.WarehouseInstance import WarehouseInstance
from tables.ProductInstance import ProductInstance


from sqlalchemy.orm import Mapped, mapped_column

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from base.DatabaseDriver import *

# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#combining-association-object-with-many-to-many-access-patterns
class WarehouseItemDBEntry:
    __tablename__ = "WarehouseItem"

    warehouse_id: Mapped[int] = mapped_column(ForeignKey("Warehouse.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("Product.id"),
        primary_key=True
    )
    extra_data: Mapped[Optional[str]]

    # # association between Assocation -> Child
    # child: Mapped["ProductInstance"] = relationship(back_populates="product_warehouse")
    #
    # # association between Assocation -> Parent
    # parent: Mapped["WarehouseInstance"] = relationship(back_populates="products")