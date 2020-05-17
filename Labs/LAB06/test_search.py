from location import Location
from datetime import datetime
from errors import BookingError
from car import SmallCar, MediumCar, LargeCar, PremiumCar
from customer import Customer
from car_rental_system import CarRentalSystem

import pytest

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id


@pytest.fixture
def rental_fixture():
    system = CarRentalSystem()
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

@pytest.fixture
def empty_fixture():
    system1 = CarRentalSystem()
    return system1

def test_successful_search_empty_system(empty_fixture):
    assert empty_fixture.car_search(None, None) == None

def test_successful_search_nothing_matched(rental_fixture):
    list1 = rental_fixture.car_search("Audit","X41")
    i = 1
    while i in range (0,len(list1)):
        assert(rental_fixture.cars[i] == list1[i])
        i+=1
    pass

def test_successful_search_no_make_no_model(rental_fixture):

    list1 = rental_fixture.car_search(None, None)
    i = 1
    while i in range (1,len(list1)):
        assert (rental_fixture.cars[i] == list1[i])
        i+=1
    pass

def test_successful_search_no_model(rental_fixture):

    list1 = rental_fixture.car_search('Ford',None)
    i = 0
    j = 13
    while j in range (0,len(list1)):
        assert (rental_fixture.cars[j] == list1[i])
        i+=1
        j+=1
    pass


def test_successful_search(rental_fixture):

    list1 = rental_fixture.car_search('Tesla','model x')
    i = 1
    print(list1)
    while i in range (0,len(list1)):
        assert (rental_fixture.cars[19] == list1[i])
        i+=1
    pass

    