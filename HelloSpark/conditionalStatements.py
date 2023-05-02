#Comparison Operators:
#EQUAL ==
#NOT EQUAL TO  !=
#Greater than >
#Less than <
#Greter than or equal to
#Less than or eaual to
#Object identity : is

#and
#or
#not






if True:
    print('Ravindra is a good husband')
language='Java'

if language == 'Python':
    print("language is python")
else:
    print('language is not python and other language')


if language == 'python':
    print("language is python")
elif language =='Java':
    print("language is Java")
elif language =='mava':
    print('language is mava')
else:
    print("no matches found")



##Conditional operator
user ='admin'
logged_in = False

if user == 'admin' and logged_in:
    print("admin page")
else:
    print('user page')

if user == 'admin' or logged_in:
    print("admin page")
else:
    print('user page')

#Object identity

# is going to check both objects are same or different based on the object memory location
a = ['ravi']
b = ['ravi']

print(id(a))
print(id(b))
print (a == b)
print (a  is b )

#
a = ['ravi']
b = a
print(id(a))
print(id(b))
print (a is b )

##False values
#False
#None
#zero
#Any empty sequence such as [],(),{}
#Any empty mapping  for example {}

condition ='Test'
if condition:
    print ('condition is true')
else:
    print ('condition is false')

