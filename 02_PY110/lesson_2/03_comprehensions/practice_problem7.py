lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

multiples_of_three = [[num for num in sublist if num % 3 == 0] for sublist in lst]

print(multiples_of_three)