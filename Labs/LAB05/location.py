class Location:
    def __init__(self, pickup, dropoff):
        self._pickup  = pickup
        self._dropoff = dropoff

    @property
    def pickup(self):
        return self._pickup

    @property
    def dropoff(self):
        return self._dropoff

    def __str__(self):
        return f'<pickup: {self._pickup}, dropoff: {self._dropoff}>'
