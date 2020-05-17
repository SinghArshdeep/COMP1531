from flask import Flask
from src.management_system import Management_System
from src.creation import Burger, Wrap, Standard_Burger, Standard_Wrap

app=Flask(__name__)

system = Management_System()

#Add ingredients to the inventory
for i in ['Beef_patty', 'Chicken', 'Falafel', 'Bacon']:
    system.inventory.add_ingredient(i, 2, 500, 5)

for i in ['Lettuce', 'Cheese', 'Tomato', 'Beetroot', 'Mayonaise', 'Pickles', 'Onion']:
    system.inventory.add_ingredient(i, 1, 500, 5)

#Add Sides to the inventory
for i in ['Fries', 'Sweet_Potato_Chips', 'Cake', 'Cookie', 'Haloumi', 'Bacon_Bits',
          'Hash_Browns']:
    system.inventory.add_side(i, 1, 100)

#Add Sundaes to the inventory
for k in ['Chocolate', 'Strawberry']:
    system.inventory.add_sundae('Small_' + k , 1, 100)
    system.inventory.add_sundae('Medium_' + k , 2, 100)
    system.inventory.add_sundae('Large_' + k , 3, 100)


#Add Drinks to the inventory
for i in ['Vanilla_Shake', 'Chocolate_Shake', 'Dark_Chocolate_Shake', 'Brownie_Shake', 'Coke', 'Pepsi', 'Water']:
    system.inventory.add_drink(i, 1, 100)

# add standard burgers
beef_burger = Standard_Burger(4, "Beef_Burger")
for i in ['Beef_patty', 'Tomato', 'Onion', 'Cheese']:
    beef_burger.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(beef_burger)

d_beef_burger = Standard_Burger(5, "Double_Beef_Burger")
d_beef_burger.add_ingredient(system.inventory.get_ing('Beef_patty'), 2)
for i in ['Tomato', 'Onion', 'Cheese']:
    d_beef_burger.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(d_beef_burger)

vege_burger = Standard_Burger(4, "Vege_Burger")
for i in ['Falafel', 'Tomato', 'Onion', 'Beetroot']:
    vege_burger.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(vege_burger)

# add standard wraps
chicken_wrap = Standard_Wrap(4, "Chicken_Wrap")
for i in ['Chicken', 'Lettuce', 'Tomato', 'Cheese']:
    chicken_wrap.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(chicken_wrap)

bacon_wrap = Standard_Wrap(4, "Bacon_Wrap")
for i in ['Bacon', 'Lettuce', 'Tomato', 'Onion', 'Pickles']:
    bacon_wrap.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(bacon_wrap)

vege_wrap = Standard_Wrap(4, "Vege_Wrap")
for i in ['Falafel', 'Lettuce', 'Tomato', 'Mayonaise', 'Beetroot']:
    vege_wrap.add_ingredient(system.inventory.get_ing(i), 1)
system.add_standard_creation(vege_wrap)
