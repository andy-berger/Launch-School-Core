# Data generation patterns

## Table of Contents

* Linear Scan / Single Pass
* Generating All Substrings/Sublists
* Counting Frequencies with a Dictionary
* Counting Identical Pairs with a Dictionary
* Find All Unique Pairs

## Linear Scan / Single Pass

The core idea of this pattern is to solve a problem by iterating through a collection just once, from start to finish. During the scan, you maintain some state in one or more variables. With each element you visit, you update your state based on the element's value.

### Pattern

```python
def find_max(numbers):
    if not numbers:
        return None

    # 1. Initialize state: Start with the first number as the current max.
    current_max = numbers[0]

    # 2. Perform a single pass (linear scan) through the rest of the list.
    for number in numbers[1:]:
        # 3. Update state: If the current number is larger, update our max.
        if number > current_max:
            current_max = number
    
    return current_max
```
### Example

Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

```python
VOWELS = "aeiou"

def longest_vowel_substring(string):
    longest_vowel_count = 0
    curr_vowel_count = 0
    
    for char in string:
        if char in VOWELS:
            curr_vowel_count += 1
            if curr_vowel_count > longest_vowel_count:
                longest_vowel_count = curr_vowel_count
        else:
            curr_vowel_count = 0
    
    return longest_vowel_count

print(longest_vowel_substring("cwm") == 0)
print(longest_vowel_substring("many") == 1)
print(longest_vowel_substring("launchschoolstudents") == 2)
print(longest_vowel_substring("eau") == 3)
print(longest_vowel_substring("beauteous") == 3)
print(longest_vowel_substring("sequoia") == 4)
print(longest_vowel_substring("miaoued") == 5)
```

## Generating All Substrings/Sublists

This pattern is your go-to whenever a problem asks you to analyze properties of *all* substrings or sublists.

### Pattern

```python
string = "halo"
substrings = []

# Loop for the starting character
for start_idx in range(len(string)):
    # Loop for the ending character
    for end_idx in range(start_idx, len(string)):
        substrings.append(string[start_idx:end_idx + 1])

print(substrings)
# Output: ['h', 'ha', 'hal', 'halo', 'a', 'al', 'alo', 'l', 'lo', 'o']
```

### Example

Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of `'1432'`, the even-numbered substrings are `'14'`, `'1432'`, `'4'`, `'432'`, `'32'`, and `'2'`, for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

```python
def even_substrings(string):
    even_substrings_count = 0

    for start_idx in range(len(string)):
        for end_idx in range(start_idx, len(string)):
            substring = string[start_idx:end_idx + 1]
            if int(substring[-1]) % 2 == 0:
                even_substrings_count += 1
    
    return even_substrings_count

print(even_substrings("1432") == 6)
print(even_substrings("3145926") == 16)
print(even_substrings("2718281") == 16)
print(even_substrings("13579") == 0)
print(even_substrings("143232") == 12)
```

## Counting Frequencies with a Dictionary

This pattern is incredibly useful for problems involving character counts, anagrams, or finding the frequency of items in a list. The goal is to build a dictionary (or a "frequency map") where keys are the items and values are their counts.

### Pattern

```python
string = "The Flintstones Rock"
char_freq = {}

for char in string:
    if char.isalpha():
        # get(char, 0) returns the current count or 0 if the char is new.
        char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)
# Output: {'T': 1, 'h': 1, 'e': 2, 'F': 1, ...}
```

### Example

Create a function that takes a string as an argument and returns `True` if the string is a pangram, `False` if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

```python
def is_pangram(string):
    char_freq = {}

    for char in string:
        if char.isalpha():
            char = char.lower()
            char_freq[char] = char_freq.get(char, 0) + 1

    return len(char_freq) == 26

print(is_pangram("The quick, brown fox jumps over the lazy dog!") == True)
print(is_pangram("The slow, brown fox jumps over the lazy dog!") == False)
print(is_pangram("A wizard's job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard's task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard's job is to vex chumps quickly in golf.") == True)

my_str = "Sixty zippers were quickly picked from the woven jute bag."
print(is_pangram(my_str) == True)
```

## Counting Identical Pairs with a Dictionary

This pattern is extremely useful when the position of the elements doesn't matter, and you only care about the *values* themselves. It's often used for counting pairs or checking for the availability of characters.

### Pattern

```python
def pairs(numbers):
    counts = {}
    total_pairs = 0

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    for num_count in counts.values():
        total_pairs += num_count // 2
    
    return total_pairs
```

### Example

Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in `[1, 2, 3, 2, 1]` is 2: occurrences each of both `2` and `1`.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for `[1, 1, 1, 1]` and `[2, 2, 2, 2, 2]`, the function should return 2. The first list contains two complete pairs while the second has an extra `2` that isn't part of the other two pairs.

```python
def pairs(numbers):
    counts = {}
    total_pairs = 0

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    for count in counts.values():
        total_pairs += count // 2
    
    return total_pairs

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
```

## Find All Unique Pairs

This pattern is the go-to solution when a problem requires you to *compare every element in a list with every other element that comes after it*.

### Pattern

```python
numbers = [1, 2, 3]
unique_pairs = []

for first_idx in range(len(numbers)):
    for second_idx in range(idx + 1, len(numbers)):
        unique_pairs.append((numbers[first_idx], numbers[second_idx]))

print(unique_pairs)
# Output: [(1, 2), (1, 3), (2, 3)]
```

### Example

Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

```python
def closest_numbers(numbers):
    closest_pair = ()
    lowest_difference = float("inf")

    for first_idx in range(len(numbers)):
        for second_idx in range(first_idx + 1, len(numbers)):
            curr_difference = abs(numbers[first_idx] - numbers[second_idx])
            if curr_difference < lowest_difference:
                lowest_difference = curr_difference
                closest_pair = (numbers[first_idx], numbers[second_idx])
    
    return closest_pair

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
```
