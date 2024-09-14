"""students = ["Hermione", "Harry", "Ron"]"""

"""print(students[0])
print(students[1])
print(students[2])"""

"""for student in students:
    print(student)"""

"""for i in range(len(students)):
    print(i+1,students[i])"""

"""students = {
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}"""

"""print(students["Hermione"])"""
# With dictionary, you don't need to use index position to call out the data,
# as you can see here I called hermione to get her house

"""for student in students:
    print(student, students[student], sep=", ")"""
# When we use for loop to call dictionary it only returns keys not values


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"],student["house"], student["patronus"], sep=", ")