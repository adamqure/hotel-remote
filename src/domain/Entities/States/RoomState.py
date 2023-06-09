from enum import Enum

class RoomState(Enum):
    READY_FOR_CHECK_IN = 1
    UNAVAILABLE = 2
    AVAILABLE = 3
