holidays = {}
active = True

while active:
    name = input("\nКак звать? _")
    holiday = input(f"Куда поедем, {name.title()}? _")
    holidays[name] = holiday

    repeat = input("\nСледующий (yes/no)? _")
    if repeat == "no":
        active = False

print("\n ----------- Результаты -----------")
for name, holiday in holidays.items():
    print(f"{name.title()} поедет в {holiday.title()}.")

