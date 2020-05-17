from abc import ABC
from src.errors import check_amount

class Creation(ABC):
    def __init__(self):
        self._ingredients = {}
    
    @property
    def ingredients(self):
        return self._ingredients

    def add_ingredient(self, new, amt):
        check_amount(new, amt)
        
        self._ingredients[new] = amt
        
    def __str__(self):
        output = ""
        for i in self._ingredients:
            output += "{}x {} at ${} each\n".format(str(self._ingredients[i]), i.name, i.price)
        return output
    
    def show_creation(self):
        print (self.__str__())
        
    def cost(self):
        c = 0
        for i in self._ingredients:
            c += i.calculate_cost(self._ingredients[i])
        return c
       

class Burger(Creation):
    def __init__(self):
        self._base_cost = 2
        super().__init__()

    def __str__(self):
        return "Burger contains: \n" + super().__str__()
    
    def cost(self):
        return self._base_cost + super().cost()
        

class Wrap(Creation):
    def __init__(self):
        self._base_cost = 1
        super().__init__()
        
    def __str__(self):
        return "Wrap contains: \n" + super().__str__()

    def cost(self):
        return self._base_cost + super().cost()

class Standard_Creation(Creation):
    def __init__(self, cost, name):
        self._cost = cost
        self._name = name
        super().__init__()
    
    @property
    def name(self):
        return self._name
    
    def cost(self):
        return self._cost

    def add_ingredient(self, ing, amt):
        self._ingredients[ing] = amt

    def __str__(self):
        output = ""
        for i in self._ingredients:
            output += "{}x {}\n".format(str(self._ingredients[i]), i.name)
        return output

    def contains(self):
        output = ""
        for i in self._ingredients:
            output += "{}\n".format(i.name)
        return output

class Standard_Burger(Standard_Creation):
    def __init__(self, cost, name):
        super().__init__(cost, name)

    def __str__(self):
        return self.name + " contains:\n" + super().__str__()

class Standard_Wrap(Standard_Creation):
    def __init__(self, cost, name):
        super().__init__(cost, name)
    
    def __str__(self):
        return self.name + " contains:\n" + super().__str__()
