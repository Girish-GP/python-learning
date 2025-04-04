# write a program to generate multiplication table from 2 to 20 and write them to different files .Place  these files in a folder

import os

folder_path = "multiplication-table"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def multiplicationTable(num):
    # file_path = os.path.join(folder_path,f"{num}_table.txt")
    file_path =f"{folder_path}/{num}_table.txt"
    with open(file_path,"w") as f:
        for i in range(1,11):
            f.write(f"{num} x {i} = {num*i}\n")
    
for i in range(2,21):
    multiplicationTable(i)
