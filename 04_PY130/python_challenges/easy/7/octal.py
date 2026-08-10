class Octal:
    def __init__(self, octal_number):
        self.octal_number = octal_number
    
    def to_decimal(self):
        if not self.octal_number.isdigit():
            return 0

        decimal_number = 0
        curr_exponent = 0
        for digit in self.octal_number[::-1]:
            if not self.is_valid_digit(digit):
                return 0

            decimal_number += int(digit) * 8 ** curr_exponent
            curr_exponent += 1
        
        return decimal_number
    
    @staticmethod
    def is_valid_digit(digit):
        return digit not in ["8", "9"]