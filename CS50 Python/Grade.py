score = int(input("Score: "))

# Version 1
"""if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Score B")
elif score >= 70 and score < 80:
    print("Score C")
elif score >= 60 and score < 70:
    print("Score D")
else:
    print("Grade: F")"""

# Version 2
"""if 90 <= score and score <= 100:
    print("Grade: A")
elif 80 <= score and score < 90:
    print("Score B")
elif 70 <= score and score < 80:
    print("Score C")
elif 60 <= score and score < 70:
    print("Score D")
else:
    print("Grade: F")"""

# Version 3
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
