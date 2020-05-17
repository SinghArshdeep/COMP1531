import pytest
from src.creation import Burger, Wrap, Standard_Burger, Standard_Wrap
from src.item import Ingredient, Side, Drink
from src.errors import LimitError, QuantityError, check_amount
from src.order import Order
from src.management_system import Management_System

''' Order Management System tests'''
class TestOrderManagement():
    def setup_method(self):
        self.sys = Management_System()
    
    def test_initial_setup(self): #US6/7
        assert self.sys.order_id == 0
        assert len(self.sys.current_orders) == 0
        assert len(self.sys.completed_orders) == 0
    
    def test_update_status(self): #US7
        for i in range (10):
            self.sys.add_order()
        
        self.sys.update_order_status(3)
        self.sys.update_order_status(5)
        self.sys.update_order_status(1)
        
        assert len(self.sys.current_orders) == 7
        assert len(self.sys.completed_orders) == 3

    def test_get_order(self): #US6
        self.o1 = self.sys.add_order()
        self.o2 = self.sys.add_order()
        o1 = self.sys.get_order(1)
        assert(o1 == self.o1)

''' Visual Tests - view orders (US7) '''
def setup_order():
    order = Order(1)
    order.add_side(Side("Fries", 1, 10), 1)
    order.add_side(Side("Cake", 3, 10), 2)
    order.add_drink(Drink("Juice", 3, 10), 2)
    order.add_drink(Drink("Soda", 3, 10), 1)
    burger = Burger()
    burger.add_ingredient(Ingredient("Patty", 1, 10), 1)
    burger.add_ingredient(Ingredient("Cheese", 1, 10), 2)
    order.add_creation(burger)
    return order

o = setup_order()
print (str(o))
print (o.status_str())
o.set_status(True)
print (o.status_str())

''' Visual Tests - view all orders (US7) '''
def setup_system():
    sys = Management_System()
    
    #Set up Inventory
    sys.inventory.add_drink("Juice", 1, 10)
    sys.inventory.add_drink("Soda", 1, 10)
    sys.inventory.add_drink("Water", 1, 10)
    
    sys.inventory.add_ingredient("Patty", 1, 11)
    sys.inventory.add_ingredient("Falafel", 1, 11)
    sys.inventory.add_ingredient("Cheese", 1, 11)
    sys.inventory.add_ingredient("Tomato", 1, 11)
    sys.inventory.add_ingredient("Carrot", 1, 11)
    sys.inventory.add_ingredient("Lettuce", 1, 11)
    sys.inventory.add_ingredient("Chilli", 1, 11)
    
    sys.inventory.add_side("Fruit", 1, 11)
    sys.inventory.add_side("Fries", 1, 11)
    sys.inventory.add_side("Cake", 1, 11)
    
    #Add Orders
    sys.add_order()
    sys.add_order()
    sys.add_order()
    sys.add_order()
    
    #Set up Order details
    o1 = sys.current_orders[0]
    o2 = sys.current_orders[1]
    o3 = sys.current_orders[2]
    o4 = sys.current_orders[3]
    
    o1.add_side(sys.inventory.sides[0], 2)
    o1.add_drink(sys.inventory.drinks[0], 1)
    o1.add_creation(Burger())
    o1.creations[0].add_ingredient(sys.inventory.ingredients[0], 2)
    o1.creations[0].add_ingredient(sys.inventory.ingredients[3], 1)
    o1.creations[0].add_ingredient(sys.inventory.ingredients[5], 1)
    
    o2.add_side(sys.inventory.sides[1], 1)
    o2.add_drink(sys.inventory.drinks[1], 1)
    o2.add_creation(Wrap())
    o2.creations[0].add_ingredient(sys.inventory.ingredients[2], 1)
    o2.creations[0].add_ingredient(sys.inventory.ingredients[1], 2)
    o2.creations[0].add_ingredient(sys.inventory.ingredients[5], 1)
    
    
    o3.add_side(sys.inventory.sides[0], 2)
    o3.add_drink(sys.inventory.drinks[0], 1)
    o3.add_creation(Burger())
    o3.creations[0].add_ingredient(sys.inventory.ingredients[0], 2)
    o3.creations[0].add_ingredient(sys.inventory.ingredients[4], 1)
    o3.creations[0].add_ingredient(sys.inventory.ingredients[6], 1)
    
    o4.add_side(sys.inventory.sides[0], 2)
    o4.add_drink(sys.inventory.drinks[0], 1)
    o4.add_creation(Burger())
    o4.creations[0].add_ingredient(sys.inventory.ingredients[0], 2)
    o4.creations[0].add_ingredient(sys.inventory.ingredients[2], 1)
    o4.creations[0].add_ingredient(sys.inventory.ingredients[3], 1)
    
    return sys

''' Test Show Current Orders - Multiple Orders'''
sys = setup_system()
sys.show_current_orders()

''' Test Check Order Status - Incomplete '''
sys.check_order_status(1)

'''Test Show Current Orders - None '''
sys.update_order_status(1)
sys.update_order_status(2)
sys.update_order_status(3)
sys.update_order_status(4)
sys.show_current_orders()
