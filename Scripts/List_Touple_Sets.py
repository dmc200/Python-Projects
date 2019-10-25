# List Examples
'''
courses = ["History", "Math", "Physics", "ComSci"]
courses_2 = ["Education", "Statistics"]

courses.append("Art")

courses.insert(0, courses_2)

print(courses[0])

print(courses)

courses.remove(courses_2)

courses.extend(courses_2)

print(courses)

courses.remove("Math")

print(courses)

popped = courses.pop()

print(popped)

print(len(courses))
print(courses[2])
print(courses[-1])
'''

'''
courses = ["History", "Math", "Physics", "ComSci"]
courses_2 = ["Education", "Statistics"]

print(courses.index("History"))

new_list = sorted(courses)
print(new_list)

print("Art" in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)
'''

'''
courses = ["History", "Math", "Physics", "ComSci"]

# change what seperates items in a list with .join()
course_str = ' - '.join(courses)
print(course_str)

# turn back to a string
course_str = course_str.split(" - ")
print(course_str)
'''


# Lists are Mutable.
# Touples are Imutable.

'''
touple_1 = ('history', 'english', 'math')

touple_2 = touple_1
mtset = {"math", "math", "ComcSci", "English", "ComSci"}
mtset2 = {"math", "History", "Art", "English", "Reddit"}

print(mtset)

mtset.intersection(mtset2)
# touple_1[1] = 'art'

print(touple_1)
print(touple_2)
print(mtset)
print(mtset2)

mtset = {"math", "math", "ComcSci", "English", "ComSci"}
mtset2 = {"math", "History", "Art", "English", "Reddit"}
'''

cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}

# Sets are optimized for boolean operations like this:
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))


empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # incorrect, this will create a dictionary.
empty_set = set()  # correct way to start an empty set.
