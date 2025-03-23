temp = {1,43,23}
#len(s) : Returns the length of the set
print(f"Length of set temp is {len(temp)}") # 3

#remove(1) : removes 1 from the set and updates the set
temp.remove(1)
print(f"Set after removing 1 : {temp}") # {43,23}

#add(1) : adds 1 to the set and updates it
temp.add(1)
print(f"Set after adding 1 : {temp}") # {43,23,1}

#union({23,33,124}) : Return a new set with all items of both set
temp2= temp.union({23,3,33})
print(f"Union of sets : {temp2}") #{1,33,3,23,43}

#intersection({23}) : Returns a new set with common elements
temp3 = temp.intersection({23})
print(f"Intersection of sets : {temp3}") # { 23}

#clear() : clears the set
temp.clear()
print(f"Set after clearing : {temp}") # set()

