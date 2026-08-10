class RomanNumeral:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number
    
    ROMAN_NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def to_roman(self):
        roman_number = ""
        remaining = self.decimal_number

        for key, value in self.__class__.ROMAN_NUMERALS.items():
            multiplier, remainder = divmod(remaining, value)
            if multiplier > 0:
                roman_number += key * multiplier
            remaining = remainder

        return roman_number

romannumeral = RomanNumeral(600)
print(romannumeral.to_roman())