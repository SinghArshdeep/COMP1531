from location import Location
from booking import Booking
from car import *
from customer import Customer
from num2words import num2words

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []
        self._nbooking = 0

    def make_booking(self, customer, car, period, location):
        self._nbooking += 1
        self._customers.append(customer)
        self._cars.append(car)
        new_booking = Booking(customer, car, period, location)
        new_booking.calculate_fee()
        self._bookings.append(new_booking)
        
        print('~~~ Make ' + num2words(self._nbooking, to = 'ordinal') + ' booking ~~~')
        print('=== Booking Successful! ===')
        print('Booking details:')
        print(new_booking)
        print('=== Thank you for using Affordable Rentals ===')
        print('\n')

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        for car in self._cars:
            if car.rego is rego:
                return car
        return None

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
