dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
# merged = dict1 | dict2
dict1.update(dict2)
# print(f"Merging using | operator : {merged}")
print(f"Merging using dict method update : {dict1}")

# we can open multiple file instances using with statement

with (
    open("text1.txt","w") as f1,
    open("text2.txt","w") as f2
):
    f1.write("This is text file 1")
    f2.write("This is text file 2")
