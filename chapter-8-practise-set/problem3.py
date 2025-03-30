#How do you prevent a python print() function to print a new line at the end


#To prevent the print() function in Python from printing a new line at the end, you can use the end parameter, which allows you to specify what should be printed at the end instead of the default newline character (\n).


print('Hello',end="")
print('World')
# HelloWorld


print("Hello",end = " ")
print("World")
# Hello World


print("Hello",end = "-")
print("World")
# Hello-World