class Customer:
    def __init__(self, name, license):
        self._name = name
        self._license = license

    @property
    def name(self):
        return self._name

    @property
    def license(self):
        return self._license

    def __str__(self):
        return f'<name: {self._name}, license: {self._license}>'
