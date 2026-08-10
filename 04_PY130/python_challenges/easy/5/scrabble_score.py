class Scrabble:
    SCORES = {
        "aeioulnrst": 1,
        "dg": 2,
        "bcmp": 3,
        "fhvwy": 4,
        "k": 5,
        "jx": 8,
        "qz": 10,
    }

    def __init__(self, word):
        self.word = word.lower() if isinstance(word, str) else ""
      
    def score(self):
        total = 0

        for letter in self.word:
            for score_letter, score_value in self.__class__.SCORES.items():
                if letter in score_letter:
                    total += score_value
        
        return total
    
    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()