student ={'name':'Ravindra','designanation':'SSE','place':'bangalore'}
print(student['name'])
print(student['designanation'])

student ['name']='Saritha'
student ['designanation']='software engineer'
print(student)
student.update({'name':'Ravindra','designation':'Senior software enginner','mobno':'6309509379'})
print(student)
del student['mobno']
print(student)
student.pop('name')
print(student)
print(len(student))
print(student.items())


##How to loop through the dictionaries
for key,value in student.items():
    print(key,value)