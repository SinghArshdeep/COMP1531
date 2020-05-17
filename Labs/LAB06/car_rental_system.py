from booking import Booking
from location import Location
from errors import BookingError, check_booking_error
from datetime import datetime, date

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    '''
    Query Processing Services
    '''
    def car_search(self, name=None, model=None):
        
        found = 0
        if len(self._cars) == 0:
            return None
        
        if name is None and model is None:
            return self._cars
        
        new_list = []
        
        if model is None:
            for car in self._cars:
                if car.name is name:
                    found = 1
                    new_list.append(car)
        
        if name is None:
            for car in self._cars:
                if car.model == model:
                    found = 1
                    new_list.append(car)
          
        for car in self._cars:
            if car.name is name and car.model == model:
                found = 1
                new_list.append(car)

        if int(found) == 0:
            return self._cars

        return new_list
          

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        
        for car in self._cars:
            if car.rego is rego:
                new_car = car
                return new_car
        return None
    '''
    Booking Services
    '''

    def make_booking(self, customer, car, start_date,end_date, start_location, end_location):
        
        try:
            Check = check_booking_error(start_date,end_date, start_location, end_location)
        except BookingError as err:
            return err
        else:
            
            location = Location(start_location, end_location)
            
            d1 = datetime.strptime(start_date, "%Y-%m-%d")
            d2 = datetime.strptime(end_date, "%Y-%m-%d")
            period = abs((d2 - d1).days) + 1
        
            new_booking = Booking(customer, car, period, location)
            new_booking.apply()
            print('=== Booking Successful! ===')
            print('Booking details:')
            print(new_booking)
            print('=== Thank you for using Affordable Rentals ===')
        
            self._bookings.append(new_booking)

            return new_booking
        

    def check_fee(self, customer, car, date1, date2, location1, location2):
        try:
            Check = check_booking_error(start_date,end_date, start_location, end_location)
        except BookingError as err:
            print(err)
        else:
        
            d1 = datetime.strptime(start_date, "%Y-%m-%d")
            d2 = datetime.strptime(end_date, "%Y-%m-%d")
            period = abs((d2 - d1).days)
        
            fee = period * car.calc_fee(period)
        
        return fee
        
    ''' 
        Registration Services
    '''
    def add_car(self, car):
        self._cars.append(car)

    def add_customer(self, customer):
        self._customers.append(customer)


    '''
    Properties
    '''
    @property
    def cars(self):
        return self._cars

    @property
    def customers(self):
        return self._customers

    @property
    def bookings(self):
        return self._bookings

