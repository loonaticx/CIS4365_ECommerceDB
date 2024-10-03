from dataclasses import dataclass

from tables import PersonalInfoInstance
from tables import AccountInstance

from typing import Union


@dataclass
class CustomerInstance:
    """
    A local Customer instance, not dependent on the database.
    """
    personal_info: PersonalInfoInstance
    account: Union[bool, AccountInstance] = None

