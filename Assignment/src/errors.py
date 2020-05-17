class IDError(Exception):
    def __init__(self, msg=None):
        if msg == None:
            msg = "Invalid ID."
        super().__init__(msg)

class LimitError(Exception):
    pass

class QuantityError(Exception):
    pass

class ItemNameError(Exception):
    pass

class ItemPriceError(Exception):
    pass

class ItemQuantityError(Exception):
    pass

class ItemLimitError(Exception):
    pass

class IngredientError(Exception):
    pass

''' validation methods '''
def check_amount(itm, amt):
    #check amount before adding
    if itm.limit != None and itm.limit < amt:
        raise LimitError
    
    if itm.total_quantity < amt:
        raise QuantityError
        
def check_new_item(name, price, quantity, limit = None):
    if not isinstance(name, str):
        raise ItemNameError
    
    if any(i.isdigit() for i in name):
        raise ItemNameError
    
    if price < 0:
        raise ItemPriceError
        
    if quantity < 0:
        raise ItemQuantityError
        
    if limit != None and limit < 0:
        raise ItemLimitError
        
def check_update_errors(amount):
    if type(amount) != int:
        raise ItemQuantityError
    
