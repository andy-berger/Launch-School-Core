class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        anagrams = []

        for candidate in possible_anagrams:
            candidate_lower = candidate.lower()
            if not candidate_lower == self.word:

                if sorted(candidate_lower) == sorted(self.word):
                    anagrams.append(candidate)
        
        return anagrams