# list = [1,2,4]

# for item in list:
#     print(item)
# else:
#     print("done")

list = [1, 2, 4]

for item in list:
    if item == 2:
        print("Found 2!")
        break
else:
    print("Number not found.")
