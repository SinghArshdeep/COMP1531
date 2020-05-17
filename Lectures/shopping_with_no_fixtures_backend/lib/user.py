from flask_login import UserMixin

from lib.cart import Cart


class User(UserMixin):
    __id = -1

    def __init__(self, username, password, cart=None):
        self._id = self._generate_id()
        self._username = username
        self._password = password
        self._cart = cart if cart is not None else Cart()
        self._admin = False

    @property
    def username(self):
        return self._username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, status):
        self._admin = status

    def get_id(self):
        """Required by Flask-login"""
        return str(self._id)

    def _generate_id(self):
        User.__id += 1
        return User.__id

    @classmethod
    def set_id(cls, id):
        cls.__id = id

    def validate_password(self, password):
        return self._password == password

    @property
    def cart(self):
        return self._cart
