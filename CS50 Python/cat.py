# Create a program which "meows" 3 times

"""print("meow")
print("meow")
print("meow")"""

# Variation 2

"""i = 5
while i !=0:
    print("meow")
    i = i-1"""

# Variation 3

"""i = 1
while i <= 3:
    print("meow")
    i = i+1"""

# Variation 4

"""i = 0
while i < 3:
    print("meow")
    i += 1"""
    # More succinct way included in the code for i = i+1

# For loop variation 1

"""for i in [0,1,2]:
    print("meow")"""

# For loop variation 2

"""for _ in range(3):
    print("meow")"""

# Variation 3
"""print("meow\n" *3, end="")"""

# variation 4
"""while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
