numbers = [1, 2, 3, 4, 5]

new_numbers = []
index = len(numbers) - 1
while index >= 0:
    new_numbers.append(numbers[index])
    index -= 1

print(new_numbers)

print(numbers[::-1])

print(list(reversed(numbers)))