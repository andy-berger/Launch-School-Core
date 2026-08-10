class Series:
    def __init__(self, digits):
        self.digits = digits
    
    def slices(self, length):
        if length > len(self.digits):
            raise ValueError("Slice length must be smaller than or equal the length of digits.")
        
        result = []
        for start_idx in range(len(self.digits) - length + 1):
            chunk = self.digits[start_idx:start_idx + length]
            result.append([int(ch) for ch in chunk])

        return result