from dataclasses import dataclass, field
from tables.ProductInstanceDBEntry import ProductInstanceDBEntry


@dataclass
class PurchaseRecordInstance:
    """
    A local facility instance, not dependent on the database.
    """
    # uuid handled by inventory
    # customer_id handled by DBEntry
    # product_id handled by DBEntry
    product: ProductInstanceDBEntry
    quantity: int
    # status

    """
    purchase_date: str
    purchase_time: str
    purchase_price: float
    purchase_total: float
    purchase_tax: float
    purchase_discount: float
    purchase_final: float
    purchase_status: str
    purchase_notes: str
    purchase_invoice: str
    purchase_tracking: str
    purchase_shipped: bool
    purchase_shipped_date: str
    purchase_shipped_tracking: str
    purchase_shipped_notes: str
    purchase_shipped_received: bool
    purchase_shipped_received_date: str
    purchase_shipped_received_notes: str
    purchase_shipped_received_signature: str
    purchase_shipped_received_signature_date: str
    purchase_shipped_received_signature_notes: str
    purchase_shipped_received_signature_image: str
    """

