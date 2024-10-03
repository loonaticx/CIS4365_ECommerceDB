from tables.user.AccountInstance import AccountInstance
from tables.user.CustomerInstanceDBEntry import CustomerInstanceDBEntry
from tables.user.PersonalInfoInstance import PersonalInfoInstance
from base.DatabaseDriver import *
personal_info = PersonalInfoInstance(
    first_name = "John",
    middle_initial = "D",
    last_name = "Doe",
    phone_number = "1234567890",
    address = "1234 Elm St",
    zip_code = "12345"
)

cust_account = AccountInstance(
    username = "",
    email = "em",
    pass_hash = "",
    registered_on = "",
    last_login = ""
)


class CustomerGenerator:

    def __init__(self, database):
        self.database = database
        create_account = False

    def _generateCustomer(self) -> CustomerInstanceDBEntry:
        return CustomerInstanceDBEntry(personal_info, cust_account)

    def generateCustomers(self, numCustomers:int=1):
        generatedCustomers = []
        for _ in range(numCustomers):
            customer = self._generateCustomer()
            self.database.generateEntry(customer)
            generatedCustomers.append(customer)
        return generatedCustomers



if __name__ == "__main__":
    """
    Driver code; when ran, will insert arbitrary day care entries into the database.
    """
    # Generate our DB
    # database = DatabaseManager(Config)
    # database.initSession()

    customerAmt = 1
    for generatedCustomer in CustomerGenerator(Database).generateCustomers(customerAmt):
        Database.generateEntry(generatedCustomer)
    print(f"Generated {customerAmt} customers!")
