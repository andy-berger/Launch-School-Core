lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sublists_sorted = [sorted(sublist, key=str) for sublist in lst]

print(sublists_sorted)