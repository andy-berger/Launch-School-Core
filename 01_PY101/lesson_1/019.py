def oddities(elements):
    output = []
    i = 0
    while i < len(elements):
        if i % 2 == 0:
            output.append(elements[i])
        i += 1

    return output

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4]) == [1, 3])
print(oddities(["abc", "def"]) == ['abc'])
print(oddities([123]) == [123])
print(oddities([]) == [])
