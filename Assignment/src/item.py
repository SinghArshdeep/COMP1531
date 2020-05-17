from abc import ABC
from src.errors import QuantityError, LimitError

class Item(ABC):
    def __init__(self, name, price, quant, lim = None):
        self._name = name
        self._price = price
        self._total_quantity = quant
        self._limit = lim
        
        
    ''' properties'''
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def total_quantity(self):
        return self._total_quantity
    
    @property
    def limit(self):
        return self._limit
            
    def calculate_cost(self, amt):
        if amt < 0:
            raise ValueError
        return amt*self._price

    def update_quantity(self, amt):
        if amt < 0:
            if abs(amt) > self._total_quantity:
                raise QuantityError
        self._total_quantity += amt
    
    def update_quantity_staff(self, amt):
        self._total_quantity += amt

    def __str__(self):
        output = 'Name: ' + self._name
        output += '\nPrice: ' + str(self._price)
        output += '\nLimit: ' + str(self._limit)
        return output


    ''' Validation Functions'''
    def check_amount(self, amt):
        if self._limit != None and amt > self._limit:
            raise LimitError
        elif amt > self._total_quantity:
            raise QuantityError
        return True
    
    

class Ingredient(Item):
    def __init__(self, name, price, quant, lim = None):
        super().__init__(name, price, quant, lim)
        
    def __str__(self):
        return "Ingredient " + super().__str__()

class Side(Item):
    def __init__(self, name, price, quant, lim = None):
        super().__init__(name, price, quant, lim)
        
    def __str__(self):
        return "Side " + super().__str__()

class Drink(Item):
    def __init__(self, name, price, quant, lim = None):
        super().__init__(name, price, quant, lim)
    
    def __str__(self):
        return "Drink " + super().__str__()

class Sundae(Item):
    def __init__(self, name, price, quant, lim = None):
        super().__init__(name + '_' + 'Sundae', price, quant, lim)
    
    def __str__(self):
        return self._name + '\nPrice: ' + str(self._price) + '\nLimit: ' + str(self._limit)
