nums = [1,2,5,9,10,3]
print(nums)

print(max(nums))
print(min(nums))
print(sum(nums))
nums.sort()
nums.sort(reverse=True)
print(nums)
sortednums=sorted(nums)
print(nums)
print(sortednums)


courses = ['History','Math','Physics','CompSci']
#it will loop through the list and it will print the list one by one
for item in courses:
    print(item)

##if you wantedd to get index along withe elements in a list then we can use enumarate function in python
for index, item in enumerate(courses, start=1):
    print(index, item)

##How to convert the list into Strings

ListofString= ','.join(courses)
print(ListofString)
new_list = ListofString.split(',')
print(new_list)

#Use Case: If you wanted to store and modify the values then you can use the Lists
#list methods append clear copy count extend index insert pop remove reverse sort
##List extend for loop and +
##Lists are used to store multiple items in a single variable
##lists are used to create using square brackets
##lists are ordered and mutable and allow duplicate values
##lists index starts with [0] and so on and if you give the index which is not there then it will throw an error
##if you wanted to check the value is present or not in the list use the 'in' and 'not in ' operator to check it will give boolean value true or false

##Use Case of tuples if you wanted to access only elements once you have created then that time we can use the tuple
##Tuples are immutable and it can not be changed once it is created
##Tuple can be crated using ()
tuple_1 = ('math','sci','com','it')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0]='art' ##we can not add elements to tuple in python

##Sets are not going to allow duplicate values
#Sets are used to create with {} brackets

set_1 = {'math','sci','art','math'}
set_2 = {'comm','design','art','math'}
print(set_1)
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))
print('math' in set_1)

##How to create a empty list
empty_list = []
empty_list1 =list()

##How to create a empty  tuples
empty_tuple= ()
empty_tuple

##How to create a empty sets
#empty_set ={} #this is not the right way
empty_set =set()
