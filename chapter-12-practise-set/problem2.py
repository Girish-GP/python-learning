# write a program to print third , fifth , seventh element of a list using enumerate function

list1 = [1,2,3,4,5,6,7]

for index,item in enumerate(list1):
    if (index == 2 or index == 4 or index == 6) and item != None:
        print(item)
else:
    print("End of the list")
