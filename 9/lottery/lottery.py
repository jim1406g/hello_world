"""Модуль содержит класс Lottery - лотерея."""

import string
import random

class Lottery():
    """Модель лотереи."""

    def __init__(self, count_number=10, count_char=5):
        """
        count_number - количество натуральных чисел от 1 в лотрее,
        count_char - количество символов a, b, ...
        """
        backlog = list(range(1,11))
        backlog.extend(string.ascii_lowercase[0:5])
        self.backlog = tuple(backlog)
        print(f"Лотерея на последовательности {self.backlog}.")

    def play(self, length=4):
        """Играть лотерею. len - длина выигрышной последовательности. Возвращает выигрышную последовательность в Tuple."""
        win = []
        while len(win) < length:
            win.append(random.choice(self.backlog))
        win = tuple(win)
        print(f"Выигрышная комбинация: {win}")
        return win
