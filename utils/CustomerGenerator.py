from tables.CustomerInstanceDBEntry import CustomerInstanceDBEntry
from tables.PersonalInfoInstance import PersonalInfoInstance

personal_info = PersonalInfoInstance(
    first_name = "John",
    middle_initial = "D",
    last_name = "Doe",
    phone_number = "1234567890",
    address = "1234 Elm St",
    zip_code = "12345"
)

class CustomerGenerator:

    def __init__(self, database):
        self.database = database

    def _generateCustomer(self) -> FacilityInstanceDBEntry:
        return CustomerInstanceDBEntry(personal_info)



if __name__ == "__main__":
    """
    Driver code; when ran, will insert arbitrary day care entries into the database.
    """
    # Generate our DB
    # database = DatabaseManager(Config)
    # database.initSession()

    facilityAmt = 2
    for genDaycare in DaycareGenerator(Database).generateDaycares(facilityAmt, (1, 10)):
        Database.generateEntry(genDaycare)
    print(f"Generated {facilityAmt} daycares!")
