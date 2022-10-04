from dataclasses import dataclass

from models.addresss import Address


@dataclass
class Merchant:
    """
    class for tracking merchant information
    """
    name: str
    address: Address
    phone: str
    website: str
