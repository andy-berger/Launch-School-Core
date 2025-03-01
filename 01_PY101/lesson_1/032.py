def clean_up(string):
    result = ""
    previous_char = ""
    for char in string:
        if not char.isalpha():
            char = " "
        if char == " " and previous_char == " ":
            continue
        result += char
        previous_char = char

    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
