import uuid

class Person:
    def __init__(self, name: str, emailAddress: str, id: uuid = uuid.uuid4()):
        self._name = name
        self._emailAddress = emailAddress
        self._id = id