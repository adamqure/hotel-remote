import uuid
from datetime import datetime

class RoomCharge:
    def __init__(self, itemName, unitCost, count, creator):
        self.itemName = itemName
        self.unitCost = unitCost
        self.count = count
        self.creator = creator
        self.id = uuid.uuid4()
        self.date = datetime.now