from dataclasses import dataclass, field


@dataclass
class ProductInstance:
    """
    A local facility instance, not dependent on the database.
    """
    name: str = "Unknown"
