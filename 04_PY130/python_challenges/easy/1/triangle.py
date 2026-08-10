class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        self.sides_sorted = sorted(self.sides)

        if any(side <= 0 for side in self.sides):
            raise ValueError("This is not a triangle (all sides must be of length > 0).")
        
        if self.sides_sorted[0] + self.sides_sorted[1] <= self.sides_sorted[2]:
            raise ValueError("This is not a triangle (the sum of the lengths of any two sides must be greater than the length of the third side).")

    @property
    def kind(self):
        unique_sides = len(set(self.sides))
        if unique_sides == 1:
            return "equilateral"
        elif unique_sides == 2:
            return "isosceles"
        
        return "scalene"