numbers = range(1,21)
for number in numbers:
    print(number)


million_numbers = range(1,1000001)
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

odd_numbers = range(1,20,2)
print(list(odd_numbers))

print(list(range(3,31,3)))

cube = [value**3 for value in range(1,11)]
print(cube)
