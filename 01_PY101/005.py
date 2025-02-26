bill = float(input("What is the bill? "))
tip_percentage = float(input("What is the tip percentage? "))
tip_amount = bill / 100 * tip_percentage

print(f"\nThe tip is ${tip_amount:.2f}")
print(f"The total is ${bill + tip_amount:.2f}")
