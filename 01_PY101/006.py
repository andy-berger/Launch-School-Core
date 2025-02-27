import math

num = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')
if operation == "s":
    result = f"The sum of the integers between 1 and {num} is {sum(range(1, num + 1))}."
elif operation == "p":
    result = f"The product of the integers between 1 and {num} is {math.prod(range(1, num + 1))}."

print(f"\n{result}")
