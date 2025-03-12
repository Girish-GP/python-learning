datalist = ["ggp",7,False,4.2]
print(datalist[0])
datalist[0] = 'xyz' #unlike strings , list are mutable
print(datalist[0])

temp = "str"
# temp[0] = 'z' 'str' does not support item assignment but list does

#slicing in lists
print(datalist[0:3]) # ['xyz',7,False]