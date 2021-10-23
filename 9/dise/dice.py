"""Модуль содержит класс Dice, моделирующий игральный кубик."""

import random

class Dice():
    """Игральный кубик."""

    def __init__(self, sides=6):
        """sides - количество граней."""
        if(sides < 6):
            print("Количество граней меньше 6, принудительно выставляем - 6")
            self.sides = 6
        else:
            self.sides = sides

    def roll_dice(self):
        """Выводит случайное число 1..sides"""
        print(f"Бросок... Результат: {random.randint(1, self.sides)} из {self.sides}")
