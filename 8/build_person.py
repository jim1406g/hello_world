def build_person(first_name, last_name, middle_name='', age=None):
    """Возвращает информацию о человеке."""
    person = {'first_name': first_name, 'last_name': last_name, 'middle_name': middle_name}
    if age:
        person['age'] = age
    return person


men1 = build_person('Вася', 'Пупкин')
men2 = build_person('Дюша', 'Жуйкин', 'Мамин')
men3 = build_person('Кака', 'Кукуйкин', age=100)

print(men1)
print(men2)
print(men3)
