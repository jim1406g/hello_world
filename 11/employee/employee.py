class Employee():
    """Класс Работник предприятия."""
    def __init__(self, first_name, last_name, salary):
        """Создать работника Имя, Фамилия, Зарплата."""
        self.first_name = first_name
        self.lastname = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        """Поднять зарплату."""
        self.salary += increase

    def get_salary(self):
        return self.salary