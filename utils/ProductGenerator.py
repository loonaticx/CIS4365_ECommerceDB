
from base.DatabaseDriver import *
from tables.ProductInstanceDBEntry import ProductInstanceDBEntry
from tables.ProductInstance import ProductInstance
from tables.WarehouseInstance import WarehouseInstance
from tables.PurchaseRecordInstanceDBEntry import PurchaseRecordInstanceDBEntry
from tables.PurchaseRecordInstance import PurchaseRecordInstance
from tables.WarehouseInstanceDBEntry import WarehouseInstanceDBEntry

import random



class ProductGenerator:

    def __init__(self, database):
        self.database = database

    def _generateProduct(self) -> ProductInstanceDBEntry:
        return ProductInstanceDBEntry(ProductInstance(name="gay"))

    def generateProducts(self, productAmt: int):
        generatedProducts = []
        for _ in range(productAmt):
            product = self._generateProduct()
            self.database.generateEntry(product)
            generatedProducts.append(product)
        return generatedProducts

    def _generatePurchaseRecord(self, product: ProductInstanceDBEntry, quantity=1) -> PurchaseRecordInstanceDBEntry:
        return PurchaseRecordInstanceDBEntry(PurchaseRecordInstance(product=product, quantity=quantity))

    def generatePurchases(self, productInfo:dict):
        generatedPurchases = []
        for productEntry, quantity in productInfo.items():
            purchaseRecord = self._generatePurchaseRecord(productEntry)
            self.database.generateEntry(purchaseRecord)
            generatedPurchases.append(purchaseRecord)
        return generatedPurchases


"""
maybe search code later

        for productEntry, quantity in productInfo.items():
            product = self.database.query(ProductInstanceDBEntry).filter(ProductInstanceDBEntry.name == productEntry).first()
            for _ in range(quantity):
                purchaseRecord = self._generatePurchaseRecord(product)
                self.database.generateEntry(purchaseRecord)

"""

if __name__ == "__main__":
    """
    Driver code; when ran, will insert arbitrary day care entries into the database.
    """
    # Generate a warehouse now
    warehouse = WarehouseInstance()
    warehouseDB = WarehouseInstanceDBEntry(warehouse)

    # Generate our DB
    # database = DatabaseManager(Config)
    # database.initSession()

    productAmt = 2
    # ProductGenerator(Database).generateProducts(productAmt)
    productsXCount = {

    }
    for generatedProduct in ProductGenerator(Database).generateProducts(productAmt):
        Database.generateEntry(generatedProduct)
        productsXCount[generatedProduct] = random.randint(1, 10)

    ProductGenerator(Database).generatePurchases(productsXCount)

    print(f"Generated {productAmt} products!")


