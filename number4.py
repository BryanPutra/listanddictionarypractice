eren = {"name": "Eren", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0],"tests": [75.0, 90.0]}
mikasa = {"name": "Mikasa", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0],"tests": [89.0, 97.0]}
armin = { "name": "Armin", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
students = [eren, mikasa, armin]
for student in students:
    print(student['name'])
    print(student['homework'])
    print(student['quizzes'])
    print(student['tests'])

def average(num):
    total = sum(num)
    total = float(sum(num))
    return total/len(num)
print(average(students[2]['homework']))

def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return ((10/100)*homework)+((30/100)*quizzes)+((60/100)*tests)
print(get_average(students[1]))

def get_letter_grade(score):
    if score >=90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: return "F"

print(get_letter_grade(get_average(students[0])))

def get_class_average(students):
    results = []
    for student in students:
        x = get_average(student)
        results.append(x)
    return results

print(get_class_average(students))
classaverage = (80.55 + 91.14999999999999 + 79.9) / 3
print(get_letter_grade(classaverage))

