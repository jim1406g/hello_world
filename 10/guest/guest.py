"""Программа Гость."""

filename = 'guest_book.txt'
greeting = 'Здравствуйте! Введите, пожалуйста, Ваше имя (для выхода введите exit): '

with open(filename, 'a') as f:
    while True:
        guest = input(greeting)
        if guest == 'exit':
            break
        else:
            f.write(f"{guest.title()}\n")
