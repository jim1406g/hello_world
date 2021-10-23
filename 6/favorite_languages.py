developers = [
    'jen',
    'sarah',
    'bob',
    'phil',
    'edward',
]

favorite_languages = {
    'jen': 'python',
    'sarah': 'groovy',
    'bob': 'c++',
}

for developer in developers:
    if developer in favorite_languages:
        print(f"Thank you {developer.title()} for taking the survey! Your choice is {favorite_languages[developer].title()}!")
    else:
        print(f"{developer.title()}, take the survey, please!")
