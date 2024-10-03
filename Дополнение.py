grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_a = sorted(students)
grades_a = []
for n in grades:
    a = sum(n)/ len(n)
    grades_a.append(a)
the_final =zip(students_a, grades_a)
print(dict(the_final))