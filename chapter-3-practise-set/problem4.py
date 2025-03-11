#write a program to replace double space in a string with single spaces
test = input("enter string:")
print(f"Whether {test} contains double space ? {test.count(' ') == 2}") 
print("replace with single space",test.replace('  ',' ').count(' ') == 1)