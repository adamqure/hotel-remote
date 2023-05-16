import uuid

class Person:
    def __init__(self, name, emailAddress):
        self._name = name
        self._emailAddress = emailAddress
        self._id = uuid.uuid4()