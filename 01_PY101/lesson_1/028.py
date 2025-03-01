def triangle(width):
    spaces = width - 1
    stars = 1
    for i in range(width):
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 1

triangle(5)
triangle(9)
