lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_of_odd_numbers(sublist):
    odd_numbers = [num for num in sublist if num % 2 != 0]
    return sum(odd_numbers)

odd_sorted = sorted(lst, key=sum_of_odd_numbers)

print(odd_sorted)