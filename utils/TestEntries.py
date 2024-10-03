from base.DatabaseDriver import *


# Test account
from tables.user.AccountInstanceDBEntry import AccountInstanceDBEntry
from tables.user.AccountInstance import AccountInstance
testAccount = AccountInstance(
    username = "test",
    email = "",
    pass_hash = "",
    registered_on = "",
    last_login = ""
)
testAccountDB = AccountInstanceDBEntry(testAccount)
Database.generateEntry(testAccountDB)



from tables.user.CustomerInstanceDBEntry import CustomerInstanceDBEntry
from tables.user.PersonalInfoInstance import PersonalInfoInstance
personalInfo = PersonalInfoInstance(
    first_name = "test",
    last_name = "test",
    phone_number = "test",
    address = "test",
    zip_code = "test",
)

testCustomerDB = CustomerInstanceDBEntry(personalInfo)
Database.generateEntry(testAccountDB)
print(testAccountDB)


print(testAccountDB)
