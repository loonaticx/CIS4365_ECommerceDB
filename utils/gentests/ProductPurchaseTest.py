from base.DatabaseDriver import *

from tables.ProductInstance import ProductInstance
from tables.ProductInstanceDBEntry import ProductInstanceDBEntry
from tables.PurchaseRecordInstance import PurchaseRecordInstance


product_test = ProductInstance(
    name = "test"
)

product_testDB = ProductInstanceDBEntry(product_test)


purchase_record = PurchaseRecordInstance(
    product = product_testDB,
    quantity = 1
)

print(purchase_record)