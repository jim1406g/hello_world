"""Модуль Ресторан"""

class Restaurant():
    """Модель ресторана."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация атрибутов."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Вывод описания ресторана."""
        print(f"Restaurant {self.restaurant_name.title()} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Открыть ресторан."""
        print(f"Restaurant {self.restaurant_name.title()} is open.")

    def set_number_served(self, number):
        """Установить общее количество посетителей."""
        self.number_served = number

    def increment_number_served(self, day_number):
        """Добавить к общему количество посетителей за день."""
        self.number_served += day_number
