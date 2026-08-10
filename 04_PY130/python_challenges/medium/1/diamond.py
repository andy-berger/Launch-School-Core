class Diamond:  
    @classmethod
    def make_diamond(cls, letter):
        upper_range = list(chr(i) for i in range(65, ord(letter) + 1))
        lower_range = list(chr(i) for i in range(65, ord(letter)))[::-1]
        full_range = upper_range + lower_range

        diamond_width = cls._max_width(letter)

        return "\n".join([cls._make_row(let).center(diamond_width) for let in full_range]) + "\n"
    
    @classmethod
    def _make_row(cls, letter):
        if letter == "A":
            return "A"
        
        return letter + cls._determine_spaces(letter) + letter
    
    @classmethod
    def _determine_spaces(cls, letter):
        return " " * (2 * (ord(letter) - ord("A")) - 1)
    
    @classmethod
    def _max_width(cls, letter):
        if letter == "A":
            return 1

        return 2 * (ord(letter) - ord("A")) + 1