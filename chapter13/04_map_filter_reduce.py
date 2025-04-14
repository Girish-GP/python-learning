from functools import reduce

l = [1,2,3,4,5]

squareList = lambda x: x*x

temp = map(squareList,l) # map a function squareList on l and return a new lit object 

print(list(temp)) # [1,4,9,16,25]
print(l)


even = lambda x: x%2 == 0

temp1 = filter(even,l)
print(list(temp1))
print(l)

sum = lambda a,b : a+b

temp2 = reduce(sum,l)
print(temp2)