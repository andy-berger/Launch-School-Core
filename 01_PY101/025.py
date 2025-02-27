def crunch(string):
    prev_char = ""
    new_string = ""
    for char in string:
        if char == prev_char:
            continue

        prev_char = char
        new_string += char

    return new_string

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
