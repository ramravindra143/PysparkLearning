nums = [1,2,3,4]
'''for num in nums:
    print (num)'''

for num in nums:
    if num == 3:
        print("num")
        continue
    print(num)

##Nested Loops
for num in nums:
    for letter in 'abc':
        print(letter, num)

#how to give the range of loop
for i in range(1,101):
    print(i)

#How to use the while loop
x = 0
while True:
    if x ==5:
        break
    print(x)
    x += 1