##we can create a function without having any code in it but make sure we need to use pass keyword in function
def hello_func():
    pass
print(hello_func())
##if you call the function with out using paranthesis automatically it will give you memory location of the function print(hello_func)

def hello_func1():
    print('hello python glad to learn you!')

#DRY Dont repeat yourself
hello_func1()
hello_func1()
hello_func1()
hello_func1()

def hello_Pfunction():
    return 'hello world I am learning new language'

message = hello_Pfunction()
print(message)
print(hello_Pfunction().upper())
