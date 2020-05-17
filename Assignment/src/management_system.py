from src.order import Order
from src.inventory import Inventory
from src.item import Ingredient, Side, Drink
from src.creation import *
from src.errors import IDError


class Management_System():
    order_id = 0

    def generate_order_id(cls):
        cls.order_id += 1
        return cls.order_id

    def __init__(self):
        self._temp_orders = []
        self._current_orders = []
        self._completed_orders = []
        self._inventory = Inventory()
        self._standard = []

    ''' Properties '''
    @property
    def temp_orders(self):
        return self._temp_orders
    
    @property
    def current_orders(self):
        return self._current_orders

    @property
    def completed_orders(self):
        return self._completed_orders

    @property
    def inventory(self):
        return self._inventory

    @property
    def standard_creations(self):
        return self._standard

    ''' Public Methods '''
    def confirm_order(self, order):
        self._current_orders.append(order) #add to curr orders for staff
        self._temp_orders.remove(order) #remove from the temp orders
    
    #adds a new order to the current orders list
    def add_order(self):
        order = Order(self.generate_order_id())
        self._temp_orders.append(order)
        return order

    #adds standard burger into the standard listed
    def add_standard_creation(self, creation):
        self._standard.append(creation)

    #shows the current status of a given order
    def check_order_status(self, check_id):
        order = self.find_order_status(check_id)
        
        if order == None:
            raise IDError
        
        return order


    #   updates the status of an order and moves from current to completed
    #   assumes the order is in the current order list and is being marked
    #   as a complete order
    def update_order_status(self, update_id):
        for order in self._current_orders:
            if order.id == update_id:
                order.set_status(True)
                self.current_orders.remove(order)
                self.completed_orders.append(order)
                return

    # displays all current orders
    def show_current_orders(self):
        if len(self.current_orders) == 0:
            print("No current orders")
        else:
            print("Current Orders")
            for order in self.current_orders:
                print (order)

    # updates the inventory based on an order
    def update_inventory(self, order):
        for i in order.drinks:
            name = i.name
            self.inventory.update_item(name, -order.drinks[i])
        for i in order.sides:
            name = i.name
            self.inventory.update_item(name, -order.sides[i])
        for c in order.creations:
            for i in c.ingredients:
                name = i.name
                self.inventory.update_item(name, -c.ingredients[i])


    def remove_inventory_creation(self, creation):
        for c in creation.ingredients:
            name = c.name
            self.inventory.update_item(name, -creation.ingredients[c])

    def remove_inventory_item(self, item, amt):
        name = item.name
        self.inventory.update_item(name, -amt)

    def readd_to_inventory(self, order):
        for i in order.drinks:
            name = i.name
            self.inventory.update_item(name, order.drinks[i])
        for i in order.sides:
            name = i.name
            self.inventory.update_item(name, order.sides[i])
        for c in order.creations:
            for i in c.ingredients:
                name = i.name
                self.inventory.update_item(name, c.ingredients[i])


    def get_standard_creation(self, name):
        for i in self.standard_creations:
            if i.name == name:
                return i
        return None
       

    def get_order(self, id):
        for i in self.temp_orders:
            if i.id == int(id):
                return i
        for i in self.current_orders:
            if i.id == int(id):
                return i
        for i in self.completed_orders:
            if i.id == int(id):
                return i
        return None

    def remove_order(self, order):
        if order in self.temp_orders:
            self._temp_orders.remove(order)
        elif order in self.current_orders:
            self._current_orders.remove(order)
        elif order in self._completed_orders:
            self._completed_orders.remove(order)

    '''
    Private Methods
    Not to be accessed outside the class
    '''
    # find an order given it's ID
    def find_order_status(self, check_id):
        for order in self._temp_orders:
            if order.id == check_id:
                return order
        for order in self._current_orders:
            if order.id == check_id:
                return order
        for order in self._completed_orders:
            if order.id == check_id:
                return order
        #if it reaches here an invalid id was entered
        raise IDError
        return None
