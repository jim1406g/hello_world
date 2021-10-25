file_name = 'war_and_peace.txt'
pattern = 'Andrew'

try:
    with open(file_name) as f:
        lines = f.readlines()
        count = 0
        line = ''
        for line in lines:
            count += line.lower().count(pattern.lower())
        print(f"В книге {file_name} содержится {count} вхождений слова '{pattern}'.")
except:
    print(f"Файл {file_name} не найден!")