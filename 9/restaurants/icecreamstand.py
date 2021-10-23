"""Модуль Киоск Мороженое"""

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Модель киоска с мороженым"""
    def __init__(self, restaurant_name, flavors = ['vanilla',]):
        super().__init__(restaurant_name, 'IceCream')
        self.flavors = flavors

    def describe_flavors(self):
        print(self.flavors)
