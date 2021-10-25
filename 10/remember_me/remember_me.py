"""Приветствие пользователя по имени."""

import json


def load_username(filename):
    """Загрузить имя пользователя из файла"""
    try:
        with open(filename) as f:
            return json.load(f)['username']
    except:
        return None


def get_new_username(filename):
    """Запросить и сохранить имя пользователя."""
    username = input(f"Введите имя пользователя: ")
    with open(filename, 'w') as f:
        json.dump({'username': username}, f)


def greet_user(filename):
    """Приветствовать пользователя."""
    user = None
    while not user:
        check = 'no'
        user = load_username(filename)
        if user:
            check = input(f"Ваше имя {user.title()} (yes/no)? ")
        if check != 'yes':
            user = None
            get_new_username(filename)
    print(f"Привет {user.title()}!")


greet_user('user.json')