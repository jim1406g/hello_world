"""Суматор для суммирования двух чисел."""

print("Для выхода введите 'exit'...")
while True:
    str1 = input('Первое слагаемое: ')
    if str1 == 'exit':
        break
    else:
        str2 = input('Второе слагаемое: ')
        if str2 == 'exit':
            break
    try:
        a = int(str1)
        b = int(str2)
    except ValueError:
        print('Вы ввели не число!\n')
    else:
        c = a + b
        print(f"Сумма чисел: {c}\n")
