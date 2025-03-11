#write a program to detect double space in a string
test = input("enter string:")
print(f"Whether {test} contains double space ? {test.count(' ') == 2}") 
print(f"Whether {test} contains double space ? {test.find('  ') != -1}") 