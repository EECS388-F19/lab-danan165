students = ['dana', 'adamm', 'jennifer']
students.sort()

first_name = students[0]
print(first_name)

first_name = first_name[:-1]
print(first_name)

print(max(students, key=len))