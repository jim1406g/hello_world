"""Применение класса Employee."""

from employee import Employee

he = Employee('Алексей', 'Пупкин', 1000)
print(f"Зарплата до повышения: {he.get_salary()}")
he.give_raise()
print(f"Зарплата после повышения: {he.get_salary()}")
