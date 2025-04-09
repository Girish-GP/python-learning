# := is walrus operator which performs the assignment and expression check at the same time 
if (n:= len([3,4,3,24,5])) > 3:
    print("Length of list is greater than 3")

# Without using walrus := operator 
# n = len([3,4,3,23,5])
# if n > 3:
#     print("Length of list is greater than 3")
