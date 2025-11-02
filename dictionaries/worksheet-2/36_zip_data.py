students = ['A', 'B']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]

result = {student: dict(zip(subjects, score_row)) for student, score_row in zip(students, scores)}

print(result)