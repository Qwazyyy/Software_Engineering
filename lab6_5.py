def sort_students_by_total_score(students):
    sorted_students = sorted(students, key=lambda student: -(student["exam_score"] + student["homework_score"]))
    return sorted_students


students = [
    {"name": "Alice", "exam_score": 90, "homework_score": 85},
    {"name": "Bob", "exam_score": 80, "homework_score": 90},
    {"name": "Charlie", "exam_score": 90, "homework_score": 80},
]

sorted_students = sort_students_by_total_score(students)
print(sorted_students)

empty_students = []
sorted_empty_students = sort_students_by_total_score(empty_students)
print(sorted_empty_students)

single_student = [{"name": "Eve", "exam_score": 100, "homework_score": 95}]
sorted_single_student = sort_students_by_total_score(single_student)
print(sorted_single_student)

