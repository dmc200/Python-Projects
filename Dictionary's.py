# Dictionary's Allow you to work with Key-Value Pair'str
# the Key is the data that describes the data attached to itself.
student = {'name': 'John', 'age': 25, 'courses': ["Math", "ComSci"]}

print(student['courses'])

student_2 = {1: 'John', 'age': 25, 'courses': ["Math", "ComSci"]}

print(student_2.get('phone', 'Not Found'))  # Not found is the default if none exists


# student['phone'] = '555-5555'
# student['name'] = 'Jane'
#  student.update({'name': 'Jane', 'age': '26', 'phone': '777-7777'})


age = student.pop('age')
print(age)
print(student)

print(len(student))

print(student.keys())

for key, value in student.items():
    print(key, value)
