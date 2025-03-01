def get_grade(grade1, grade2, grade3):
    mean = (grade1 + grade2 + grade3) / 3
    if mean < 60:
        return "F"
    elif mean < 70:
        return "D"
    elif mean < 80:
        return "C"
    elif mean < 90:
        return "B"
    else:
        return "A"

print(get_grade(95, 90, 93) == "A")
print(get_grade(50, 50, 95) == "D")
