# write a program to find out the line number where pyrhon is present in last problem

with open("problem6_log.txt") as f:
   content_list = f.readlines()
   line = 1
   for content in content_list:
    if 'python' in content:
        print(f"Python is present in line number {line}")
        break
    line +=1
   else:
    print("Python is not present")