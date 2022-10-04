from dataclasses import dataclass
from typing import Union


@dataclass
class Address:
    country: str
    state_type: Union["Province","State"]
    state: str
    city: str
    zip_code: str
