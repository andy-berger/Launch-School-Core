numbers = [1, 2, 3, 4]

del numbers[:]
print(numbers)

numbers = [1, 2, 3, 4]

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

print(numbers)