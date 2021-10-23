source_list = ['Миша', 'Гриша', '124', '356', '11', 0, 15]
for element in source_list:
    if (str(element).lower() == 'гриша') or (str(element).lower() == '0'):
        print(f'Внимание! Мы получили {element}!')
    else:
        print(element)
print('')
nums_list = source_list[-5:]
for num in nums_list:
    if int(num) >= 15:
        print(f'Внимание! Мы получили {num}!')
    else:
        print(num)
