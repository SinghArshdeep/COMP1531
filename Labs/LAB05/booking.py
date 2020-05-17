class Booking:
    def __init__(self, customer, car, period, location):
        self._customer = customer
        self._car = car
        self._period = period
        self._location = location
        self._fee = 0

    @property
    def customer(self):
        return self._customer
    
    @property
    def car(self):
        return self._car
    
    @property
    def period(self):
        return self._period
    
    @property
    def location(self):
        return self._location

    @property
    def fee(self):
        return self._fee

    def calculate_fee(self):
        period = self._period
        if self._car.type is 'Small' or self._car.type is 'Medium':
            self._fee = (self._car.fee)*(period)
        
        elif self._car.type is 'Large':
            self._fee = (self._car.fee)*(period)
            
            if self._period > 7:
                self._fee = self._fee*0.95

        elif self._car.type is 'Premium':
            self._fee = 1.15*(self._car.fee)*(period)
            
            if self._period > 7:
                self._fee = self._fee*0.95

        return self._fee

    def __str__(self):
        return f'Made by Customer {self._customer} \n Reserve {self._car} \n Locations: {self._location} \n Total fee: ${self._fee}'


