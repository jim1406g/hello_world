current_number = 0
while current_number < 12:
    current_number += 1
    if current_number % 2 == 0:
        continue
    if current_number == 9:
        print("break")
        break
    print(current_number)

# while True:
#     print("Press Ctrl+C...")
