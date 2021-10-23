rivers = {
    'nile': 'egypt',
    'irtish': 'russia',
    'volga': 'russia',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print('\nWe saw rivers:')
for river in rivers.keys():
    print(f"\t{river.title()}")

print('\nThese rivers runs through countries:')
for country in set(rivers.values()):
    print(f"\t{country.title()}")
