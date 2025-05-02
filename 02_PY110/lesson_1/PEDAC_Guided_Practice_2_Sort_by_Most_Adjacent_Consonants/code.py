def count_max_adjacent_consonants(string):
    cleaned_string = "".join(char for char in string if char.isalpha())
    max_consonants_count = 0
    adjacent_consonant_string = ""

    for char in cleaned_string:
        if char not in {"a", "e", "i", "o", "u"}:
            adjacent_consonant_string += char
            if len(adjacent_consonant_string) > max_consonants_count:
                max_consonants_count = len(adjacent_consonant_string) if len(adjacent_consonant_string) > 1 else max_consonants_count
        elif char in {"a", "e", "i", "o", "u"} and len(adjacent_consonant_string) > max_consonants_count:
            max_consonants_count = len(adjacent_consonant_string) if len(adjacent_consonant_string) > 1 else max_consonants_count

            adjacent_consonant_string = ""

    return max_consonants_count

def sort_by_consonant_count(string_list):
    string_list.sort(key=count_max_adjacent_consonants, reverse=True)
    return string_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']