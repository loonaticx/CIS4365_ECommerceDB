from dataclasses import dataclass

from tables.user.PersonalInfoInstance import PersonalInfoInstance
from tables.user.AccountInstance import AccountInstance

from typing import Union


@dataclass
class CustomerInstance:
    """
    A local Customer instance, not dependent on the database.
    """
    personal_info: PersonalInfoInstance
    account: Union[bool, AccountInstance] = None


