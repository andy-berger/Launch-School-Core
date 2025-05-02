VOWELS = ['a', 'e', 'i', 'o', 'u']

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []

for key in dict1:
    for word in dict1[key]:
        for char in word:
            if char in VOWELS:
                list_of_vowels.append(char)

list_of_vowels2 = [char for key in dict1 for word in dict1[key] for char in word if char in VOWELS]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

print(list_of_vowels2)