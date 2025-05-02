# Problem
Determine number of adjacent consonants in strings and sort them by highest number of adjacent consonants.

Inputs: List of strings
Output: Sorted list by highest number of adjacent consonants

Explicit rules:
- Adjacent consonants are consonants next to each other in the same word or in adjacent words (seperated by a space).
- Words are seperated by a single spaces.
- Keep original order if two strings contain the same number of adjacent consonants.

Questions:
- Can empty strings be in the input list?
- Can special characters such as periods or commas be ignored?

# Examples (Test cases)
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

# Data structures
Lists containing strings

# Algorithm
Count adjacent consonant in each string and preserve the count:
- Count consonants next to each other in each word
- Count consonants at the beginning or end of the word if there is an adjacent consonant in the previous or next word.

Sort by number of adjacent consonants (descending) and build new sorted list.

Return new sorted list.

# Code
See file code.py