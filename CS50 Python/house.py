name = input("what's your name? ")

# Variation 1

"""if name == "Harry":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")"""

# Variation 2

"""if name == "Harry" or name == "Ron" or name == "Hermione":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")"""

# Variation 3

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")