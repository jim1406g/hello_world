"""Класс Analise - анализ комбинаций лотереи."""

import lottery

class LotteryAnalise(lottery.Lottery):
    """Модель лотереи с анализом."""

    def analise(self, combination):
        """Распечатывает сложность для комбинации cpmbination - List или Tuple"""
        combination = tuple(combination)
        length = len(combination)
        reply_count = 0
        win = []
        while combination != win:
            reply_count += 1
            win = self.play(length)
        print(f"Потребовалось {reply_count} переборов.")
