from dataclasses import dataclass


@dataclass
class Currency:
    country_code: str
    symbol: str
