import pytest
from src.inventory import Inventory
from src.item import Ingredient, Side, Drink
from src.errors import ItemNameError, ItemPriceError, ItemQuantityError, ItemLimitError, QuantityError
from src.order import Order

''' Tests for inventory class functions '''
class TestInventorySetup():
    def setup_method(self):
        self.inventory = Inventory()
    
    def test_setup_blackbox(self):
        assert len(self.inventory.ingredients) == 0
        assert len(self.inventory.sides) == 0
        assert len(self.inventory.drinks) == 0
    
    def test_setup_whitebox(self):
        assert len(self.inventory._ingredients) == 0
        assert len(self.inventory._sides) == 0
        assert len(self.inventory._drinks) == 0

class TestAddItemToInventory():
    def setup_method(self):
        self.inventory = Inventory()
    
    #add ingredient
    def test_add_ingredient_with_limit(self):
        self.inventory.add_ingredient("Patty", 2, 50, 2)
        assert len(self.inventory.ingredients) == 1
    
    #add ingredient
    def test_add_ingredient_without_limit(self):
        self.inventory.add_ingredient("Patty", 2, 50)
        assert len(self.inventory.ingredients) == 1
    
    #add side
    def test_add_side(self):
        self.inventory.add_side("Fries", 1, 10)
        assert len(self.inventory.sides) == 1
    
    #add drink
    def test_add_drink(self):
        self.inventory.add_drink("Juice", 3, 10)
        assert len(self.inventory.drinks) == 1
    
    
    #   As the same function is at the beginning of each ingredient, side,
    #   and drink; the tests to check for name, price, quantity, and limit
    #   errors have been split among the three
    
    #add ingredient with invalid names
    def test_add_ingredient_invalid_names(self):
        with pytest.raises(ItemNameError):
            self.inventory.add_ingredient(10, 1, 1)
        with pytest.raises(ItemNameError):
            self.inventory.add_ingredient("1Patty", 1, 1)

    #add sides with invalid price
    def test_add_side_invalid_price(self):
        with pytest.raises(ItemPriceError):
            self.inventory.add_side("Fries", -5, 1)
    
    #add side with invalid quantity
    def test_add_side_invalid_quantity(self):
        with pytest.raises(ItemQuantityError):
            self.inventory.add_side("Fries", 1, -1)
    
    #add drink with invalid limit
    def test_add_drink_invalid(self):
        with pytest.raises(ItemLimitError):
            self.inventory.add_drink("Juice", 1, 10, 0)
            self.inventory.add_drink("Juice", 1, 0, -5)

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
    
    def test_add_to_item(self):
        #add to an ingredient
        self.inventory.update_item("Patty", 10)
        assert self.inventory.ingredients[0].total_quantity == 21
        
        #add to a side
        self.inventory.update_item("Fruit", 10)
        assert self.inventory.sides[0].total_quantity == 21
        
        #add to a drink
        self.inventory.update_item("Water", 10)
        assert self.inventory.drinks[1].total_quantity == 21
    
    
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

''' Tests for item class functions '''
class TestItemQuantityUpdate():
    def setup_method(self):
        self.ing1 = Ingredient("Cheese", 5, 40)
        self.side1 = Side("Wedges", 2, 50)
        self.drink1 = Drink("Cola", 3, 50)
    
    def test_add_to_item(self):
        self.ing1.update_quantity(10)
        assert self.ing1.total_quantity == 50
        self.side1.update_quantity(10)
        assert self.side1.total_quantity == 60
        self.drink1.update_quantity(10)
        assert self.drink1.total_quantity == 60

''' Visual tests for inventory functions (US8)'''
def create_inventory():
    inventory = Inventory()
    inventory.add_ingredient("Patty", 1, 11)
    inventory.add_ingredient("Falafel", 1, 11)
    inventory.add_ingredient("Cheese", 1, 11)
    inventory.add_ingredient("Tomato", 1, 11)
    inventory.add_ingredient("Carrot", 1, 11)
    inventory.add_ingredient("Lettuce", 1, 11)
    inventory.add_ingredient("Chilli", 1, 11)
    inventory.add_side("Fruit", 1, 11)
    inventory.add_side("Fries", 1, 11)
    inventory.add_side("Cake", 1, 11)
    inventory.add_drink("Juice", 1, 11)
    inventory.add_drink("Water", 1, 11)
    inventory.add_drink("Soda", 1, 11)
    return inventory

i = create_inventory()
i.show_inventory()


