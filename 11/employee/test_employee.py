import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""

    def setUp(self):
        """Создание экземпляра класса и задание размера повышения зарплаты."""
        self.first_salary = 0
        self.default_increase = 5000
        self.increase = 1000
        self.employee = Employee('A', 'B', self.first_salary)

    def test_give_default_rest(self):
        """Проверка увеличения зарплаты по умолчанию."""
        self.employee.give_raise()
        self.assertEqual(self.employee.get_salary(), self.first_salary + self.default_increase)

    def test_give_custom_raise(self):
        """Проверка увеличения зарплаты на выбранную величину."""
        self.employee.give_raise(self.increase)
        self.assertEqual(self.employee.get_salary(), self.first_salary + self.increase)


if __name__ == '__main__':
    unittest.main()