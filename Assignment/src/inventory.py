from src.item import Ingredient, Side, Drink, Sundae
from src.errors import check_new_item, check_update_errors

class Inventory():
    def __init__(self):
        self._ingredients = []
        self._sides = []
        self._drinks = []
        
    @property
    def ingredients(self):
        return self._ingredients
    
    @property
    def sides(self):
        return self._sides
    
    @property
    def drinks(self):
        return self._drinks
    
    def add_ingredient(self, name, price, quantity, limit = None):
        check_new_item(name, price, quantity, limit)
        
        i = Ingredient(name, price, quantity, limit)
        self._ingredients.append(i)
    
    def add_side(self, name, price, quantity, limit = None):
        check_new_item(name, price, quantity, limit)
        
        s = Side(name, price, quantity, limit)
        self._sides.append(s)
    
    def add_drink(self, name, price, quantity, limit = None):
        check_new_item(name, price, quantity, limit)
        
        d = Drink(name, price, quantity, limit)
        self._drinks.append(d)
    
    def add_sundae(self, name, price, quantity, limit=None):
        check_new_item(name, price, quantity, limit)
        
        s = Sundae(name, price, quantity, limit)
        self._sides.append(s)
    
    def __str__(self):
        
        output = ""
        
        output += "\n=== Ingredients ===\n"
        for i in self._ingredients:
            output += "{} x {}\n".format(i.total_quantity, i.name.replace('_', ' '))
            
        output += "\n=== Sides ===\n"
        
        for i in self._sides:
            output += "{} x {}\n".format(i.total_quantity, i.name.replace('_', ' '))
                
        output += "\n=== Drinks ===\n"
        
        for i in self._drinks:
            output += "{} x {}\n".format(i.total_quantity, i.name.replace('_', ' '))
        
        return output

    def get_ing(self, name):
        for i in self._ingredients:
            if i.name == name:
                return i
        return None
    
    def get_drink(self, name):
        for i in self._drinks:
            if i.name == name:
                return i
        return None
    
    def get_side(self, name):
        for i in self._sides:
            if i.name == name:
                return i
        return None
    
    def show_inventory(self):
        print (self.__str__())
    
    
    def update_item(self, name, amount):
        check_update_errors(amount) #check for an invalid amount
        
        #find list to go through
        for i in self._ingredients:
            if i.name == name:
                i.update_quantity(amount)
                return
        for i in self._sides:
            if i.name == name:
                i.update_quantity(amount)
                return
        for i in self._drinks:
            if i.name == name:
                i.update_quantity(amount)
                return


    def update_item_staff(self, name, amount):
        check_update_errors(amount) #check for an invalid amount

        #find list to go through
        for i in self._ingredients:
            if i.name == name:
                i.update_quantity_staff(amount)
                return
        for i in self._sides:
            if i.name == name:
                i.update_quantity_staff(amount)
                return
        for i in self._drinks:
            if i.name == name:
                i.update_quantity_staff(amount)
                return

