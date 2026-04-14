from enum import Enum


class  maritalstatus(str, Enum):
    MARRIED = "Married"
    SINGLE = "Single"

class HouseOwnership(str, Enum):
    RENTED = "rented"
    NORENT_NOOWN = "norent_noown"
    OWNED = "owned"
