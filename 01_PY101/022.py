def center_of(string):
    string_length = len(string)
    if string_length % 2 == 0:
        return string[string_length // 2 - 1] + string[string_length // 2]
    else:
        return string[string_length // 2]

print(center_of('I Love Python!!!') == "Py")
print(center_of('Launch School') == " ")
print(center_of('Launchschool') == "hs")
print(center_of('Launch') == "un")
print(center_of('Launch School is #1') == "h")
print(center_of('x') == "x")
