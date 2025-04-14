# write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce

list1 = [ 32,1,56,23,567,3,2]

reduceFnc = lambda a,b : max(a,b)

max_number = reduce(reduceFnc,list1)

print(max_number)
print(max(list1))