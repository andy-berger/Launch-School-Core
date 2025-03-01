def check_double_number(num):
    num = str(num)
    if len(num) % 2 == 0:
        return num[:int(len(num) / 2)] == num[int(len(num) / 2):]

    return False

def twice(num):
    if check_double_number(num):
        return num
    else:
        return num * 2

print(twice(37) == 74)
print(twice(44) == 44)
print(twice(334433) == 668866)
print(twice(444) == 888)
print(twice(107) == 214)
print(twice(103103) == 103103)
print(twice(3333) == 3333)
print(twice(7676) == 7676)
