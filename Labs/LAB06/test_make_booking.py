from location import Location
from datetime import datetime
from errors import BookingError
from car import SmallCar, MediumCar, LargeCar, PremiumCar
from customer import Customer
from car_rental_system import CarRentalSystem

import pytest
system = CarRentalSystem()

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

rego_generator = IdGenerator()
licence_generator = IdGenerator()

@pytest.fixture
def rental_fixture():
    rego_generator = IdGenerator()
    licence_generator = IdGenerator()
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore"]:
            system.add_car(SmallCar(name, model, rego_generator.next()))
            system.add_car(MediumCar(name, model, rego_generator.next()))
            system.add_car(LargeCar(name, model, rego_generator.next()))

    for name in ["Tesla", "Audi"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, rego_generator.next()))

    for name in ["Matt", "Isaac", "Taylor"]:
        system.add_customer(Customer(name, licence_generator.next()))
    
    return system
    
def test_successful_make_medium_car_booking(rental_fixture):
    print("test_successful_make_medium_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking.fee == 375

def test_successful_Location(rental_fixture):
    print("test_successful_Location")
    start_location  = 0
    end_location    = 'Melbourne'
    
    user = rental_fixture.get_customer(1)
    car  = rental_fixture.get_car(3)
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert booking.name == 'Invalid Location'

def test_successful_date(rental_fixture):
    print("test_successful_date")
    start_location  = 'Hundy'
    end_location    = 'Melbourne'
    
    user = rental_fixture.get_customer(2)
    car  = rental_fixture.get_car(12)
    
    start_date      = f'12-2018-1'
    end_date        = f'2018-12-5'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date, start_location, end_location)
    assert booking.name == 'Invalid Date'

def test_successful_no_date(rental_fixture):
    print("test_successful_no_date")
    start_location  = 'Hundy'
    end_location    = 'Melbourne'
    
    user = rental_fixture.get_customer(2)
    car  = rental_fixture.get_car(12)
    
    start_date      = f'0'
    end_date        = f'2018-12-5'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date, start_location, end_location)
    assert booking.name == 'Invalid Date'

def test_successful_Period(rental_fixture):
    print("test_successful_Period")
    start_location  = 'Rurby'
    end_location    = 'Mourne'
    
    user = rental_fixture.get_customer(2)
    car  = rental_fixture.get_car(1)
    
    start_date      = f'2018-12-9'
    end_date        = f'2018-12-5'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert booking.name == 'Invalid Period'

def test_successful_make_large_car_booking(rental_fixture):
    print("test_successful_make_large_car_booking")
    start_location  = 'Burne'
    end_location    = 'Gour'
    
    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(18)
    
    start_date      = f'2018-12-13'
    end_date        = f'2018-12-23'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 2
    assert rental_fixture._bookings[1].location.pickup == start_location
    assert rental_fixture._bookings[1].location.dropoff == end_location
    assert booking.fee == 1045

def test_successful_make_premium_car_booking(rental_fixture):
    print("test_successful_make_premium_car_booking")
    start_location  = 'yern'
    end_location    = 'forer'
    
    user = rental_fixture.get_customer(2)
    car  = rental_fixture.get_car(23)
    
    start_date      = f'2018-12-20'
    end_date        = f'2018-12-23'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 3
    assert rental_fixture._bookings[2].location.pickup == start_location
    assert rental_fixture._bookings[2].location.dropoff == end_location
    assert booking.fee == 690

def test_successful_make_small_car_booking(rental_fixture):
    print("test_successful_make_small_car_booking")
    start_location  = 'yern'
    end_location    = 'forer'
    
    user = rental_fixture.get_customer(1)
    car  = rental_fixture.get_car(16)
    
    start_date      = f'2018-12-20'
    end_date        = f'2018-12-25'
    
    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 4
    assert rental_fixture._bookings[3].location.pickup == start_location
    assert rental_fixture._bookings[3].location.dropoff == end_location
    assert booking.fee == 300


