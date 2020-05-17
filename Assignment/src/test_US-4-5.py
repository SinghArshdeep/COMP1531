import pytest
from src.management_system import Management_System
from src.creation import Burger, Wrap, Standard_Burger, Standard_Wrap
from src.order import Order
from src.item import Side, Drink, Ingredient
from src.errors import LimitError, QuantityError, IDError, ItemQuantityError
from src.inventory import Inventory

''' Order Management System tests'''
class TestOrderManagement():
    def setup_method(self):
        self.sys = Management_System()
    
    def test_add_orders(self): #US4
        self.sys.add_order()
        self.sys.add_order()
        assert len(self.sys.current_orders) == 2
        assert self.sys.current_orders[0].id == 1
        assert self.sys.current_orders[1].id == 2
    
    #US5 test for errors
    #test for successful call is under visual tests
    def test_check_status_error(self): #US5
        self.sys.add_order()
        with pytest.raises(IDError):
            self.sys.find_order_status(80)

    def test_get_order(self): #US4/5
        self.o1 = self.sys.add_order()
        self.o2 = self.sys.add_order()
        o1 = self.sys.get_order(1)
        assert(o1 == self.o1)

''' Order class tests '''
def test_initiate_order():
    order = Order(1)
    assert order.id == 1
    assert len(order.creations) == 0
    assert len(order.sides) == 0
    assert len(order.drinks) == 0
    assert order.payment_method == None
    assert order.status == False

class TestShowOrderStatus(): #US5
    def setup_method(self):
        self.order = Order(1)
        self.order.add_side(Side("Fries", 1, 10), 1)
        self.order.add_side(Side("Cake", 3, 10), 2)
        self.order.add_drink(Drink("Juice", 3, 10), 2)
        self.order.add_drink(Drink("Soda", 3, 10), 1)
        burger = Burger()
        burger.add_ingredient(Ingredient("Patty", 1, 10), 1)
        burger.add_ingredient(Ingredient("Cheese", 1, 10), 2)
        self.order.add_creation(burger)
    
    def test_status_str(self):
        assert self.order.status_str() == "Order ID 1 is currently being prepared."
        self.order.set_status(True)
        assert self.order.status_str() == "Order ID 1 is ready to be picked up."

''' Item class tests - US4'''
class TestUpdateQuantity():
    def setup_method(self):
        self.ing1 = Ingredient("Cheese", 5, 40)
        self.side1 = Side("Wedges", 2, 50)
        self.drink1 = Drink("Cola", 3, 50)
    
    def test_subtract_from_item(self):
        self.ing1.update_quantity(-10)
        self.side1.update_quantity(-10)
        self.drink1.update_quantity(-10)
        assert self.ing1.total_quantity == 30
        assert self.side1.total_quantity == 40
        assert self.drink1.total_quantity == 40
    
    def test_subtract_too_much_from_item(self):
        with pytest.raises(QuantityError):
            self.ing1.update_quantity(-70)
            self.side1.update_quantity(-70)
            self.drink1.update_quantity(-70)

''' Inventory class tests - US4'''
class TestUpdateItemInInventory():
    def setup_method(self):
        self.inventory = Inventory()
        self.inventory.add_ingredient("Patty", 1, 11)
        self.inventory.add_ingredient("Falafel", 1, 11)
        self.inventory.add_ingredient("Cheese", 1, 11)
        self.inventory.add_ingredient("Tomato", 1, 11)
        self.inventory.add_ingredient("Carrot", 1, 11)
        self.inventory.add_ingredient("Lettuce", 1, 11)
        self.inventory.add_ingredient("Chilli", 1, 11)
        self.inventory.add_ingredient("Beef Patty", 1, 11)
        self.inventory.add_side("Fruit", 1, 11)
        self.inventory.add_side("Fries", 1, 11)
        self.inventory.add_side("Cake", 1, 11)
        self.inventory.add_drink("Juice", 1, 11)
        self.inventory.add_drink("Water", 1, 11)
        self.inventory.add_drink("Soda", 1, 11)
    
    def test_remove_from_item(self):
        #add to an ingredient
        self.inventory.update_item("Carrot", -10)
        assert self.inventory.ingredients[4].total_quantity == 1
        
        #add to a side
        self.inventory.update_item("Cake", -10)
        assert self.inventory.sides[2].total_quantity == 1
        
        #add to a drink
        self.inventory.update_item("Juice", -10)
        assert self.inventory.drinks[0].total_quantity == 1
    
    def test_remove_too_much_from_item(self):
        with pytest.raises(QuantityError):
            self.inventory.update_item("Cheese", -20)
            self.inventory.update_item("Fries", -20)
            self.inventory.update_item("Soda", -20)
    
    def test_remove_non_integer(self):
        with pytest.raises(ItemQuantityError):
            self.inventory.update_item("Cheese", -2.5)
            self.inventory.update_item("Fries", -2.50)
            self.inventory.update_item("Soda", -2.60)

    def test_get_item(self):
        item = self.inventory.get_ing("Cheese")
        assert item.name == "Cheese"


''' Visual Tests - view creations (US4&5) '''
def setup_burger():
    i1 = Ingredient("Patty", 5, 10)
    i2 = Ingredient("Cheese", 1, 10)
    i3 = Ingredient("Carrot", 1.5, 10)
    i4 = Ingredient("Lettuce", 0.5, 10)
    burger = Burger()
    burger.add_ingredient(i1, 2) #10
    burger.add_ingredient(i2, 1) #1
    burger.add_ingredient(i3, 3) #4.5
    burger.add_ingredient(i4, 2) #1.0
    return burger

def setup_wrap():
    i1 = Ingredient("Falafel", 5, 10)
    i2 = Ingredient("Cheese", 1, 10)
    i3 = Ingredient("Carrot", 1.5, 10)
    i4 = Ingredient("Lettuce", 0.5, 10)
    wrap = Wrap()
    wrap.add_ingredient(i1, 2) #10
    wrap.add_ingredient(i2, 1) #1
    wrap.add_ingredient(i3, 3) #4.5
    wrap.add_ingredient(i4, 2) #1.0
    return wrap

def setup_standard_burger():
    i1 = Ingredient("Patty", 5, 10)
    i2 = Ingredient("Cheese", 1, 10)
    i3 = Ingredient("Carrot", 1.5, 10)
    i4 = Ingredient("Lettuce", 0.5, 10)
    burger = Standard_Burger(5)
    burger.add_ingredient(i1, 2)
    burger.add_ingredient(i2, 1)
    burger.add_ingredient(i3, 3)
    burger.add_ingredient(i4, 2)
    return burger

def setup_standard_wrap():
    i1 = Ingredient("Falafel", 5, 10)
    i2 = Ingredient("Cheese", 1, 10)
    i3 = Ingredient("Carrot", 1.5, 10)
    i4 = Ingredient("Lettuce", 0.5, 10)
    wrap = Standard_Wrap(5)
    wrap.add_ingredient(i1, 2)
    wrap.add_ingredient(i2, 1)
    wrap.add_ingredient(i3, 3)
    wrap.add_ingredient(i4, 2)
    return wrap

b = setup_burger()
print (str(b))

b2 = setup_standard_burger()
print(b2)

w = setup_wrap()
print (str(w))

w2 = setup_standard_wrap()
print(w2)

''' Visual tests for Order Management System (US5)'''
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

sys = setup_system()

''' Test Check Order Status - Complete '''
sys.check_order_status(4)

''' Test Check Order Status - Invalid '''
sys.check_order_status(40)

