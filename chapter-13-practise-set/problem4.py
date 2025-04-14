# write a program to filter a list of numbers which are divisble by 5.

l = [5,67,55,25,125,88,76]

filteredList = lambda x: x%5 == 0

test = filter(filteredList,l)

print(list(test))