import uuid
from datetime import datetime

class RoomCharge:
    def __init__(self, itemName, unitCost, count, creator, id: uuid = None, date: datetime = None):
        self.itemName = itemName
        self.unitCost = unitCost
        self.count = count
        self.creator = creator
        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

        if datetime == None:
            self.date = datetime.now
        else:
            self.date = date

    def __eq__(self, other):
        return self._id == other._id