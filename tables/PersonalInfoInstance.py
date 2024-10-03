from dataclasses import dataclass, field


@dataclass
class PersonalInfoInstance:
    """
    A local facility instance, not dependent on the database.
    """
    # Personal information
    first_name: str
    middle_initial: str
    last_name: str

    # Database will just store empty values for these fields
    phone_number: str
    address: str
    zip_code: str