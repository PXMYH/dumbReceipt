from dataclasses import dataclass

@dataclass
class Items:
    """
    Class for keeping track of an item information
    """
    name: str
    unit_price: float
    quantity: int = 0

    def total_price(self) -> float:
        return self.unit_price * self.quantity
