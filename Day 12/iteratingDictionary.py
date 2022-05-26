test_score = {
    'shahriar': 87,
    'kabir': 80,
    'sOhan': 95,
    'chaudhuree': 83,
    'kazi': 78,
    'sabrina': 90
}
for key, value in test_score.items():
    print(key, value)
print("\n")
for key in test_score.keys():
    print(key)
print("\n")
for value in test_score.values():
    print(value)
print("\n")

# print total of socres
total = 0
for value in test_score.values():
    total += value
print(total)
print("\n")

# max score and best student
max_score = 0
best_student = ''
for key, value in test_score.items():
    if value > max_score:
        max_score = value
        best_student = key
print(best_student, max_score)
print("\n")