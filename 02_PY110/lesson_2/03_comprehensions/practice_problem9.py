lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def numbers_are_even(item):
    for lst in item.values():
        for num in lst:
            if num % 2 != 0:
                return False

    return True

print([dictionary for dictionary in lst if numbers_are_even(dictionary)])