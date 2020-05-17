from abc import ABC
class Car(ABC):
    def __init__(self, type, brand, model, rego, fee):
        self._type = type
        self._brand = brand
        self._model = model
        self._rego = rego
        self._fee = fee
    
    @property
    def type(self):
        return self._type

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def rego(self):
        return self._rego

    @property
    def fee(self):
        return self._fee

class Small(Car):
    def __init__(self, type, brand, model, rego, fee):
        super().__init__(type, brand, model, rego, fee)

    def __str__(self):
        return "Small Car <{0}, {1}, rego: {2}>".format(self._brand, self._model, self._rego)

class Medium(Car):
    def __init__(self, type, brand, model, rego, fee):
        super().__init__(type, brand, model, rego, fee)

    def __str__(self):
        return "Medium Car <{0}, {1}, rego: {2}>".format(self._brand, self._model, self._rego)

class Large(Car):
    def __init__(self, type, brand, model, rego, fee):
        super().__init__(type, brand, model, rego, fee)

    def __str__(self):
        return "Large Car <{0}, {1}, rego: {2}>".format(self._brand, self._model, self._rego)

class Premium(Car):
    def __init__(self, type, brand, model, rego, fee):
        super().__init__(type, brand, model, rego, fee)

    def __str__(self):
        return "Premium Car <{0}, {1}, rego: {2}>".format(self._brand, self._model, self._rego)
