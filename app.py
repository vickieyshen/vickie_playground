
courses = ['History', 'Math', 'Physics', 'ComSci']
print(courses)
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[:2])
print(courses[2:])

courses.append('Art')
#courses.insert(1,'Art')
print(courses)

for index, course in enumerate(courses, start=1):
   print(index, course)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')

language = 'Java'

if language == 'Python':
    print('Lanugage is Python')
elif language == 'Java':
    print('Language is Java')
elif language =='JavaScript':
    print('Language is JavaScript')
else:
    print('no match')

while True :
     print ("hello python ")
