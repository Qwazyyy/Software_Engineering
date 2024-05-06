def improve_grades(grades):
    return [4 if grade == 3 else grade for grade in grades if grade != 2]


grades_list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

improved_grades1 = improve_grades(grades_list1)
improved_grades2 = improve_grades(grades_list2)
improved_grades3 = improve_grades(grades_list3)

print("Обновленный список оценок 1:", improved_grades1)
print("Обновленный список оценок 2:", improved_grades2)
print("Обновленный список оценок 3:", improved_grades3)
