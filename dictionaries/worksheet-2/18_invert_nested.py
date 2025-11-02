
d = {
    'math': {'john': 90, 'jane': 80},
    'science': {'john': 85, 'jane': 95}
}
r = {}
for subject, students in d.items():
    for student, score in students.items():
        if student not in r:
            r[student] = {}
        r[student][subject] = score

print(r)
