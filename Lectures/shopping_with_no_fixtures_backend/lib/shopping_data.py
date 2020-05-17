from lib.dao.inventory_dao import Warehouse
from lib.dao.user_dao import UserManager
from lib.products import *
from lib.user import *


class OnlineShoppingData:
    @classmethod
    def load_data(cls):
        warehouse = Warehouse()
        a1 = Accessories("gloves", 10, "S", "Blue")
        a2 = Accessories("kids gloves", 10, "S", "Red")
        a3 = Accessories("Glasses", 25, "M", "Pink")
        a4 = Accessories("Scarf", 50, "L", "Yellow")
        misc = Miscellaneous("Torch", 100, "1x2x3", "100kg")

        warehouse.add_item(a1)
        warehouse.add_item(a2)
        warehouse.add_item(a3)
        warehouse.add_item(a4)
        warehouse.add_item(misc)

        user_db = UserManager()

        admin = User('admin', 'admin')
        admin.admin = True
        bob = User('bob', 'bob')

        user_db.add_user(admin)
        user_db.add_user(bob)

        admin.cart.add_to_cart(0, 10)
        admin.cart.add_to_cart(1, 3)
        admin.cart.add_to_cart(2, 5)
        admin.cart.add_to_cart(4, 20)

        bob.cart.add_to_cart(0, 1)

        return warehouse, user_db
