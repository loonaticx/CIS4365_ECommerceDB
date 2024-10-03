from dataclasses import dataclass, field

from tables import CustomerInstance


@dataclass
class CustomerShoppingCart:
    """
    A local facility instance, not dependent on the database.
    """
    customer_owner: CustomerInstance
