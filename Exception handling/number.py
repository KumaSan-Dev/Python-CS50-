def main():
    x = get_int("What's x?")
    print(f"X is {x}")


"""def get_int():

    while True:
        try:
            x = int(input("What's X ?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x    # Return can break you out of a loop and will get you the value


main()"""

# Variation 2

"""def get_int():

    while True:
        try:
            return int(input("What's X ?"))
        except ValueError:
            print("x is not an integer")



main()"""


# Variation 3 with PASS
"""def get_int():

    while True:
        try:
            return int(input("What's X ?"))
        except ValueError:
            pass



main()"""


# Variation 4
def get_int(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
