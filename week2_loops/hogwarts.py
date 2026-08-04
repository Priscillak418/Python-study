# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# Iterating lists
# for i in range(len(students)):
#     print(i+1, students[i])

# Dictionary
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }


# Loops in Dictionaries
# for student in students:
#     print(student, students[student], sep=", ")


# More on dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherine", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
