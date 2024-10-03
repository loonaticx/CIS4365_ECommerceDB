from dataclasses import dataclass, field

from typing import Union


@dataclass
class WarehouseInstance:
    """
    A local Customer instance, not dependent on the database.
    """
    name: str = "Unknown"
    products: list = field(default_factory = list)
