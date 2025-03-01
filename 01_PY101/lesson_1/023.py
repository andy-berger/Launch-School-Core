def negative(num):
    return num if num < 0 else num * -1

print(negative(5) == -5)
print(negative(-3) == -3)
print(negative(0) == 0)
