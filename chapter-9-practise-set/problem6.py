# write a program to mine a log file and check if it contains python

with open("problem6_log.txt") as f:
    content = f.read()
    if python in content:
        print("python is present")
    else:
        print("python is not present")
