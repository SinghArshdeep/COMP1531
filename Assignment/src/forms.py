# read data from forms on the website
from src.order import Order
from src.item import Ingredient, Side, Drink
from src.errors import *
from src.management_system import Management_System
from src.creation import Burger, Wrap

# Class for reading the form
class CustomOrderForm():
    def __init__(self, form, inventory):
        self.order = None
        self.type = form["type"]
        self.ingredients = {}
        self.errors = {}
        self.raw = form
        self.inv = inventory

        self.parse_form()

    def parse_form(self):
        # go through all keys
        for key in self.raw:
            #non-essential keys for parsing
            if key == "form" or key == "submit_button" or key == "type":
                continue
            # order id
            elif key == "order":
                self.order = self.raw[key]
            # ingredients with a non-empty amount
            elif self.raw[key] != '':
                ing = self.inv.get_ing(key)

                try:
                    ''' check amount '''
                    if not self.raw[key].isdigit():
                        raise QuantityError
                    ing.check_amount(int(self.raw[key]))
                    
                    ''' add to ingredients list '''
                    
                    self.ingredients[key] = self.raw[key]
                
                #''' add to errors if over limit or quantity '''
                except LimitError:
                    self.errors[key] = "Amount must be between 0 and %s"%(str(ing.limit))
                except QuantityError:
                    self.errors[key] = "Amount must be between 0 and %s"%(str(ing.total_quantity))
    
        # other errors
        if self.type != "Wrap" and self.type !="Burger":
            self.errors["type"] = "Creation type must be selected"

    def create_creation(self):
        creation = Burger() if self.type == "Burger" else Wrap()
        for k, v in self.ingredients.items():
            ing = self.inv.get_ing(k)
            creation.add_ingredient(ing, int(v))
        return creation

#Separate class to handle update inventory form
class UpdateInventory():
    def __init__(self, form, inventory):
        self.errors = {}
        self.raw = form
        self.inv = inventory
        self.parse_form()

    #Goes through the form
    def parse_form(self):
        
        #Iterating through each key of the form
        for key in self.raw:
            
            if key == "submit":
                continue
            elif self.raw[key] != '':
                
                ''' checks if the amount is valid '''
                try:
                    
                    ''' add to item to the inventory '''
                    self.inv.update_item_staff(key, int(self.raw[key]))
                
#               add to errors if any exception is raised
                except ItemQuantityError:
                        self.errors[key] = "Amount is not valid. Please enter again"
                except QuantityError:
                    self.errors[key] = "Amount must be positive "

#Class for taking input from the form for the drinks
class CustomDrinkForm():
    def __init__(self, form, inventory):
        self.order = None
        self.drinks = {}
        self.errors = {}
        self.raw = form
        self.inv = inventory
        self.parse_form()
    

    def parse_form(self):
        #Iterating through each key of the form
        for key in self.raw:
            
            #non-essential keys for parsing
            if key == "submit_button" or key == "form":
                continue
            
            # order id
            elif key == "order":
                self.order = self.raw[key]
            
            #Take input if the field is not empty
            elif self.raw[key] != '':
                
                drink = self.inv.get_drink(key)
                
                try:
                    ''' check amount '''
                    if not self.raw[key].isdigit():
                        raise QuantityError

                    drink.check_amount(int(self.raw[key]))
                    ''' add to drinks list '''
                    self.drinks[key] = self.raw[key]
                
                #''' add to errors if over quantity or drink not in stock '''
                except QuantityError:
                    self.errors[key] = "Amount must be between 0 and %s"%(str(drink.total_quantity))

    # Adds the side to the order if there are no errors in parsing
    def add_drink(self, order):
        
        for i in self.drinks:
            
            drink = self.inv.get_drink(i)
            order.add_drink(drink, int(self.drinks[i]))
        
        return self.drinks

#Class for taking input from the form for the sides
class CustomSidesForm():
    def __init__(self, form, inventory):
        self.order = None
        self.sides = {}
        self.errors = {}
        self.raw = form
        self.inv = inventory
        self.parse_form()
    
    
    def parse_form(self):
        
        #Iterating through each key of the form
        for key in self.raw:
            
            #non-essential keys for parsing
            if key == "submit_button" or key == "form":
                continue
            
            # order id
            elif key == "order":
                self.order = self.raw[key]
            
            #Take input if the field is not empty
            elif self.raw[key] != '':
                side = self.inv.get_side(key)
                try:
                    ''' check amount '''
                    if not self.raw[key].isdigit():
                        raise QuantityError
                    
                    side.check_amount(int(self.raw[key]))
                    
                    ''' add to drinks list '''
                    self.sides[key] = self.raw[key]
                
                #''' add to errors if over quantity or side is not in stock'''
                except QuantityError:
                    self.errors[key] = "Amount must be between 0 and %s"%(str(side.total_quantity))

    # Adds the side to the order if there are no errors in parsing
    def add_side(self, order):
        
        for i in self.sides:
            
            side = self.inv.get_side(i)
            order.add_side(side, int(self.sides[i]))
            
        return self.sides

class StandardCreationForm():
    def __init__(self, form, sys):
        self.order = None
        self.errors = {}
        self.raw = form
        self.sys = sys
        self.creation = None
        self.parse_form()
    
    def parse_form(self):
        # go through all keys
        for key in self.raw:
            #non-essential keys for parsing
            if key == "form" or key == "submit_button" or key == "add_to_order":
                continue
            # order id
            elif key == "order":
                self.order = self.raw[key]
            # check all ingredients in a creation
            elif self.raw[key] != '':
                # find the creation
                self.creation = self.sys.get_standard_creation(key) #key is name of standard creation -> use to find item
                
                for i in self.creation.ingredients:
                    try:
                        i_name = i.name
                        ing = self.sys.inventory.get_ing(i_name)
                        ing.check_amount(self.creation.ingredients[i])
                #''' add to errors if over limit or quantity '''
                    except LimitError:
                        self.errors[key] = "The selected item is currently unavailable. Please select another option."
                    except QuantityError:
                        self.errors[key] = "The selected item is currently unavailable. Please select another option."
