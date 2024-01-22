n = int(input())
student_grades = {}

for _ in range(n):
    name, grade_as_string = input().split()
    grade = float(grade_as_string)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grade in student_grades.items():
    average_grade = sum(grade) / len(grade)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grade])}"
    print(f'{name} -> {formatted_grades} (avg: {average_grade:.2f})')
