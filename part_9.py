student = {
    "name": "Su Su",
    "age":"20",
    "score":"88",
    "pass":"true"
}

print (student["name"])
print (student["age"])
print (student["score"])
print (student["pass"])


students = [
    {"name": "Aung Aung", "score":85},
    {"name": "Su Su", "score":92},
    {"name": "Mg Mg", "score":32}
]
for student in students:
    print(student["name"],student["score"])
