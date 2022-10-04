from dataclasses import dataclass


@dataclass
class Tax:
    """
    class to track taxes
    """
    rate: int # need to do conversion to percentage
