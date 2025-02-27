def multisum(num):
    sum = 0
    for n in range(1, num + 1):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
