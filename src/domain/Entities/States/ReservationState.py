from enum import Enum

class ReservationState(Enum):
    DRAFT = 1
    RESERVED = 2
    CANCELLED = 3 
    CHECKED_IN = 4
    CHECKED_OUT = 5
    COMPLETE = 6