list_num = [1,2,3,4,34]
# index = 1
# for item in list_num:
#     print(f"Item at index {index} is {item}")
#     index += 1


for index,item in enumerate(list_num):
    print(f"Item at index {index+1} is {item}")