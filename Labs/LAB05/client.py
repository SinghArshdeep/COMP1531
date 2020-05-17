from car_rental_system import *

system = CarRentalSystem()
car1 = Small('Small', "Graham" , "Lex-9" , 1 , 24)
cus1 = Customer("Arthur" , 1)
locn1 = Location("Sydney" , "Brooks")

car2 = Large('Large', "McL" , "340XJL", 2 , 99)
cus2 = Customer("Raju" , 2)
locn2 = Location("Castle" , "Hill")

car3 = Small('Small', "Maruti" , "Swift" , 3 , 19)
cus3 = Customer("Amma" , 3)
locn3 = Location("Rouse" , "Hill")

car4 = Premium('Premium', "Mezc" , "830i" , 4 , 399)
cus4 = Customer("Sed" , 4)
locn4 = Location("Paris" , "Mysore")

car5 = Medium('Medium', "Jeep" , "Crytall" , 5 , 69)
cus5 = Customer("Aniket" , 5)
locn5 = Location("Regina" , "Toronto")

car6 = Premium('Premium', "Alpino" , "Roader" , 6 , 369)
cus6 = Customer("Blue" , 6)
locn6 = Location("Hub" , "Git")


system.make_booking(cus1 , car1 , 3 ,locn1)
system.make_booking(cus2 , car2 , 1 ,locn2)
system.make_booking(cus3 , car3 , 7 ,locn3)
system.make_booking(cus4 , car4 , 23 , locn4)
system.make_booking(cus5 , car5 , 2 , locn5)
system.make_booking(cus6 , car6 , 10 , locn6)

print("===Print all Cars===")
for item in system._cars:
    print(item)
print(end = '\n')

print("===Print all Customers===")
for item in system._customers:
    print(item)
print(end = '\n')

print("===All Bookings===")
for item in system._bookings:
    print(item)
print(end = '\n')

