#Binary files -Image
#non binary files -Text file
#there are 14 modes are available
# r --> read a file
# w --> creates and writes to a file # if file is available it will over write it
# a --> append to a file
# r+ --> read and write
# w+ --> write and read -->Most common mode
# a+ --> append and write -->Most common mode
# x  --> exclusive file concept

#if you do not specify any mode by default it will read mode
fileObj=open('firstfile.txt','w')

##Properties of a file
print(fileObj.name)
print(fileObj.mode)
print(fileObj.closed)
