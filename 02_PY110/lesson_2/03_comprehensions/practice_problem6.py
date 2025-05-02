lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

numbers_incremented = [{key: value + 1 for key, value in dictionary.items()} for dictionary in lst]

print(numbers_incremented)