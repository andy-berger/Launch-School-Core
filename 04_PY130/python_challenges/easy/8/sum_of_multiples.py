class SumOfMultiples:
    def __init__(self, *multiples):
        self.multiples = multiples if multiples else (3, 5)
    
    def to(self, number):
        return sum(x for x in range(1, number) if self._any_multiple(x))
    
    @classmethod
    def sum_up_to(cls, target_number):
        return cls().to(target_number)
    
    def _any_multiple(self, number):
        return any(number % multiple == 0 for multiple in self.multiples)