def math_operation(num1, num2, op):
    return eval(f"{num1} {op} {num2}")

def math_operations_output(num1, num2):
    for math_op in ["+", "-", "*", "/", "//", "%", "**"]:
        print(f"==> {num1} {math_op} {num2} = {math_operation(num1, num2, math_op)}")

first_num = float(input("==> Enter the first number:\n"))
second_num = float(input("==> Enter the second number:\n"))
math_operations_output(first_num, second_num)
