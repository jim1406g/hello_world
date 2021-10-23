current_users = ['doc', 'perdoc', 'zubila']
#new_users = ['zhuk', 'Zubila', 'mi-mi-mi', 'ZHopenpops']
new_users = []

if new_users:
    for new_user in new_users:
        user = new_user.lower()
        if user in current_users:
            print(f'Имя {user} уже используется, выберете другое имя!')
        else:
            print(f'Полльзователь с именем {user} может быть зарегистрирован...')
else:
    print('Задайте список пользователей!')
