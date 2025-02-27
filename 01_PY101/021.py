from datetime import datetime

age = int(input("What is your age? "))
retirement = int(input("At what age would you like to retire? "))

remaining_years = retirement - age
current_year = datetime.now().year
retirement_year = current_year + remaining_years
print(f"\nIt's {current_year}. You will retre in {retirement_year}.")
print(f"You have only {remaining_years} years of work to go!")
