from base.DatabaseDriver import *


# customer will have some redundancy.

class CustomerWishlistDBEntry(Base):
    """
    Skeleton for a db entry in the customer table.

    Will be added into the database upon init
    """

    __tablename__ = "CustomerWishlist"
    id = Column(Integer, primary_key = True, autoincrement = True)
