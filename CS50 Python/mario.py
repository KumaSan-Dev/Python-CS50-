"""print("#")
print("#")
print("#")"""

# Variation 2

"""for _ in range(3):
    print("#")"""

"""def main():
    print_column(3)

def print_column(height):
    print("#\n"* height, end="")

main()"""

# Here we are printing the question marks in mario
"""def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()"""

# Variation 3

def main():
    print_square(3)


"""def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        print()

main()"""


# Variation 4

def print_square(size):

    # For each row in square
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)

main()