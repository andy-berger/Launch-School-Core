def xor(num1, num2):
    if num1 and not num2:
        return True
    elif num2 and not num1:
        return True

    return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
