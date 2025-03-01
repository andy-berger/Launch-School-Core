def century_suffix(century_number):
    last_two = century_number % 100
    last_digit = century_number % 10

    match last_two:
        case 11 | 12 | 13:
            return "th"

    match last_digit:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"

def century(year):
    century_number = year // 100 + 1

    if year % 100 == 0:
        century_number -= 1

    suffix = century_suffix(century_number)
    return f"{century_number}{suffix}"

print(century(2000) == "20th")
print(century(2001) == "21st")
print(century(1965) == "20th")
print(century(256) == "3rd")
print(century(5) == "1st")
print(century(10103) == "102nd")
print(century(1052) == "11th")
print(century(1127) == "12th")
print(century(11201) == "113th")
