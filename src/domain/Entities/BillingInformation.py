import uuid


class BillingInformation:
    def __init__(self, fullName, streetAddress1, streetAddress2, city, state, zipCode, id: str = str(uuid.uuid4())):
        self._id = id
        self.fullName = fullName
        self.stretAddress1 = streetAddress1
        self.streetAddress2 = streetAddress2
        self.city = city
        self.state = state
        self.zipCode = zipCode