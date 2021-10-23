"""Перечисляем всех питомцев."""

files = ('cats.txt', 'dogs.txt', 'parrots.txt')

def read_file(file):
    """Читает file и возвращает содержимое. Игнорирует ошибку отсутствия файла."""
    try:
        with open(file) as f:
            content = f.read()
    except FileNotFoundError:
        content = None

    return content


for file in files:
    pets = read_file(file)
    if pets:
        print(pets.title().rstrip())
