import pytest
from src.creation import Burger, Wrap, Standard_Burger, Standard_Wrap
from src.item import Ingredient, Side, Drink
from src.errors import LimitError, QuantityError, check_amount
from src.order import Order

''' Creation class tests'''
def test_setup():
    burger = Burger()
    assert len(burger.ingredients) == 0
    
    wrap = Wrap()
    assert len(wrap.ingredients) == 0

#Test to check if the ingredients are added correctly
class TestAddIngredientToCreation(): #US2
    def setup_method(self):
        self.burger = Burger()
        self.wrap = Wrap()
        self.ing_w_limit = Ingredient("Patty", 5, 10, 2)
        self.ing_wout_limit = Ingredient("Cheese", 5, 10)
    
    def test_add_ingredient_under_lim(self):
        self.wrap.add_ingredient(self.ing_wout_limit, 1)
        assert len(self.wrap.ingredients) == 1
        assert self.wrap.ingredients[self.ing_wout_limit] == 1
        assert self.ing_wout_limit in self.wrap.ingredients
    
    def test_add_ingredient_on_limit(self):
        self.burger.add_ingredient(self.ing_w_limit, 2)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[self.ing_w_limit] == 2
        assert self.ing_w_limit in self.burger.ingredients
    
    def test_add_ingredient_over_limit(self):
        with pytest.raises(LimitError):
            self.burger.add_ingredient(self.ing_w_limit, 10)

    def test_add_ingredient_over_quantity(self):
        with pytest.raises(QuantityError):
            self.wrap.add_ingredient(self.ing_wout_limit, 20)

#Tests to check the cost of our order US3
class TestCreationCost():
    def test_empty_burger(self):
        burger = Burger()
        assert burger.cost() == 2
    
    def test_empty_wrap(self):
        wrap = Wrap()
        assert wrap.cost() == 1
    
    def test_burger_with_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Ingredient("Patty", 3, 10), 2)
        assert burger.cost() == 8
    
    def test_wrap_with_ingredient(self):
        wrap = Wrap()
        wrap.add_ingredient(Ingredient("Cheese", 1, 10), 3)
        assert wrap.cost() == 4
    
    def test_many_ingredients(self):
        i1 = Ingredient("Patty", 5, 10)
        i2 = Ingredient("Cheese", 1, 10)
        i3 = Ingredient("Carrot", 1.5, 10)
        i4 = Ingredient("Lettuce", 0.5, 10)
        burger = Burger()
        burger.add_ingredient(i1, 2) #10
        burger.add_ingredient(i2, 1) #1
        burger.add_ingredient(i3, 3) #4.5
        burger.add_ingredient(i4, 2) #1.0
        assert burger.cost() == 18.5 #total 16.5 plus base cost 2$

#Tests to check standard creations US2
class TestStandardCreations():
    def test_burger(self):
        i1 = Ingredient("Patty", 5, 10)
        i2 = Ingredient("Cheese", 1, 10)
        burger = Standard_Burger(5)
        assert(burger.cost() == 5) # check original cost is assigned
        burger.add_ingredient(i1, 1)
        burger.add_ingredient(i2, 1)
        assert(burger.cost() == 5) # check cost unchanged by adding ingredients

    def test_wrap(self):
        i1 = Ingredient("Falafel", 5, 10)
        i2 = Ingredient("Cheese", 1, 10)
        wrap = Standard_Wrap(4)
        assert(wrap.cost() == 4) # check original cost is assigned
        wrap.add_ingredient(i1, 2)
        wrap.add_ingredient(i2, 1)
        assert(wrap.cost() == 4) # check cost unchanged by adding ingredients

'''Item class tests '''
#ingredient subclass US1
def test_ing_setup_no_limit():
    i = Ingredient("Cheese", 4, 1)
    assert i.name == "Cheese"
    assert i.price == 4
    assert i.total_quantity == 1
    assert i.limit == None

def test_ing_setup_with_limit():
    i = Ingredient("Cheese", 4, 1, 10)
    assert i.limit == 10

#sides subclass US1
def test_side_setup_no_limit():
    s = Side("fries", 4, 1)
    assert s.name == "fries"
    assert s.price == 4
    assert s.total_quantity == 1
    assert s.limit == None

def test_side_setup_with_limit():
    s = Ingredient("fries", 4, 1, 10)
    assert s.limit == 10


#drinks subclass US1
def test_drink_setup_no_limit():
    d = Drink("Juice", 4, 1)
    assert d.name == "Juice"
    assert d.price == 4
    assert d.total_quantity == 1
    assert d.limit == None

def test_drink_setup_with_limit():
    d = Ingredient("Juice", 4, 1, 10)
    assert d.limit == 10

#Test calculation of individual item costs US3
class TestCalculateCostItem():
    def setup_method(self):
        self.ingredient = Ingredient("Cheese", 5, 10)
    
    def test_calculate_cost_successful(self):
        assert self.ingredient.calculate_cost(2) == 10
    
    def test_calculate_cost_negative(self):
        with pytest.raises(ValueError):
            self.ingredient.calculate_cost(-2)

''' Order class tests'''
#Test adding items to order US2
class TestAddToOrder():
    def setup_method(self):
        self.order = Order(1)
    
    def test_add_creation(self):
        new_creation = Burger()
        self.order.add_creation(new_creation)
        assert len(self.order.creations) == 1
        assert self.order.creations[0] == new_creation
    
    def test_add_multiple_creations(self):
        creation1 = Burger()
        creation2 = Wrap()
        self.order.add_creation(creation1)
        self.order.add_creation(creation2)
        assert len(self.order.creations) == 2
        assert creation1 in self.order.creations
        assert creation2 in self.order.creations
    
    def test_add_side_successful(self):
        new_side = Side("Fries", 1, 10)
        self.order.add_side(new_side, 2)
        assert len(self.order.sides) == 1
        assert self.order.sides[new_side] == 2
    
    def test_add_drink_successful(self):
        new_drink = Drink("Juice", 1, 10)
        self.order.add_drink(new_drink, 2)
        assert len(self.order.drinks) == 1
        assert self.order.drinks[new_drink] == 2
    
    def test_add_side_over_limit(self):
        new_side = Side("Fries", 1, 10, 2)
        with pytest.raises(LimitError):
            self.order.add_side(new_side, 3)

    def test_add_drink_over_limit(self):
        new_drink = Drink("Juice", 1, 10, 2)
        with pytest.raises(LimitError):
            self.order.add_drink(new_drink, 3)
    
    def test_add_side_over_quantity(self):
        new_side = Side("Fries", 1, 10)
        with pytest.raises(QuantityError):
            self.order.add_side(new_side, 20)
    
    def test_add_drink_over_quantity(self):
        new_drink = Drink("Juice", 1, 10)
        with pytest.raises(QuantityError):
            self.order.add_drink(new_drink, 20)


'''Visual Tests for US1'''
i = Ingredient("Cheese", 4, 1)
print (i.__str__())

s = Side("Fries", 2, 10, 1)
print (s.__str__())


d = Drink("Juice", 3, 10)
print (d.__str__())



