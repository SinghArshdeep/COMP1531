from src.item import Ingredient, Side, Drink
from src.creation import Burger, Wrap
from src.errors import check_amount

class Order():    
    def __init__(self, id):
        self._id = id
        self._creations = []
        self._sides = {}
        self._drinks = {}
        self._status = False
        self._payMethod = None

    
    ''' Properties '''
    @property
    def id(self):
        return self._id

    @property
    def creations(self):
        return self._creations
    
    @property
    def sides(self):
        return self._sides
    
    @property
    def drinks(self):
        return self._drinks
    
    @property
    def status(self):
        return self._status
    
    @property
    def payment_method(self):
        return self._payMethod
    
    
    '''Setters'''
    @payment_method.setter
    def set_payment_method(self, mtd):
        self._payMethod = mtd
        
    def set_status(self, stat):
        self._status = stat
    
    
    ''' methods '''
    #returns a float with the total cost of the order
    def cost(self):
        total = 0 #initialise total cost
        
        for c in self._creations:                       #add creation costs
            total += c.cost()       
        for s in self._sides:                           #add side costs
            total += s.calculate_cost(self._sides[s])
        for d in self._drinks:                          #add drink costs
            total += d.calculate_cost(self._drinks[d])
        
        return total

    # returns a string outlining the contents of the order
    def __str__(self):
        output = "Order ID " + str(self._id) + "\n------\nCreation(s):\n"
        for c in self._creations:
            output += str(c)
        output += "\n------\nSide(s):\n"
        for s in self._sides:
            output += "{}x {} at ${} each\n".format(str(self.sides[s]), s.name, s.price)
        output += "\n------\nDrink(s):\n"
        for d in self._drinks:
            output += "{}x {} at ${} each\n".format(str(self.drinks[d]), d.name, d.price)
        output += "\nTotal cost: $" + str(self.cost())    
        
        return output

    #returns a string showing the current status of the order
    def status_str(self):
        if self._status == False:
            return f"Order ID %s is currently being prepared."%(str(self._id))
        else:
            return f"Order ID %s is ready to be picked up."%(str(self._id))

    #prints the status of the order
    def show_status(self):
        print (self.status_str())

    #prints the order contents
    def show_order(self):
        print (self.__str__())

    #adds a burger or wrap to the order
    def add_creation(self, new):
        self._creations.append(new) 

    #adds a side to the order
    def add_side(self, new, amt):
        check_amount(new, amt) #make sure amount is valid
        self._sides[new] = amt #add to order

    #adds a drink to the order
    def add_drink(self, new, amt):
        check_amount(new, amt) #check amount before adding

        self._drinks[new] = amt #add to order if no exceptions raised
        
        


