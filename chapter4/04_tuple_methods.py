# count()
a = (1,2,43,43,23,23)
print(f"Number of occurences of 43 in {a} is {a.count(43)}")

#index() --> index of first occurence of element
print(f"Index of first occurence of element 23 is {a.index(23)}")

#indexing 
print(a[0])

#slicing 
print(a[0:3])

#Operations in tuple
b = (2,12,1)

#concatenation in tuple
print(f"Concatenate tuple a and b : {a+b}")

#repetition in tuple
print(f"Repetition in tuple : {a*3}")

#length in tuple
print(f"Length of {a} is {len(a)}")

#membership in tuple
print(23 in a) #True
print(1111 in a) #False