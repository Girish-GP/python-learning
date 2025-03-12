#methods in list

#append() --> append value at the end of the list
datalist.append('last')

#sort() ---> sort list in order
test = [6,2,34,21,3,6]
print(f"Unsorted list : {test}")
test.sort()
print(f"Sorted list: {test}")

#reverse() ---> to reverse the list
test.reverse()
print(f"Reversed list is : {test}")

#insert() ---> insert element at particular index
test.insert(1,89) #value 89 at index 1
print(f"New list after insertion: {test}")

#pop() ---> delete value/elememt at a particular index and returns it by default last element
test.pop(1) 
print(f"list after deleting element at index 1: {test}")

#remove() ---> Removes the first occurrence of a specific element from the list.
test.remove(6)
print(f"list after removing element 6: {test}")

#extend() ---> adds another list at the end of one list
first = [1,2,3,4]
first.extend([4,5,6,7,8])
print(f"Extended list : {first}")
first.remove(4)
print(f"Removed first occurence of 4 : {first}")

#index() ---> gives index of first occurence of an element
print(f"First occurence of element 3 in {first} is at index : {first.index(3)}")

#min() max() --> minimum & maximum element in list
print(f"Minimum element in {first} is {min(first)}")
print(f"Maximum element in {first} is {max(first)}")

#sum() --> returns sum of all elements in list
print(f"Sum of all elements in first is : {sum(first)}")

#count() --> count number of occurence of an element in a string
test2 = ['a','b','a']
print(f"Number of a in {test2} is {test2.count('a')}")

#copy() ---> to create a shallow copy of a list
new_list = first.copy()
print(f"New List : {new_list}")

#clear() ---> empty the list
first.clear()
print(f"After clear method : {first}")