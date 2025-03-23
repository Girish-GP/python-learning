#Empty set
e = set() # dont use e = {} as it will create an empty dictonary

print(type(e)) # <class 'set'>

s = {1,44,21,23,1,44}
print(s) #{1,44,21,33} duplicate elements are filtered out in sets

#properties of sets
#1] Sets are unordered => elements order does not matter
#2] Sets are unindexed => cannot access elements using their indexes
#3] There is no way to change items in sets => sets are immutable
#4] Sets cannot contain duplicate values
