def is_an_ip_number(word):
    return 0 <= int(word) <= 255

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if not (3 < len(dot_separated_words) < 5):
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address("1.2.3.4"))