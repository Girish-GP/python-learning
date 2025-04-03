#readlines() 

f = open("file.txt")
# content = f.readlines() # gives list of all lines

# print(content,type(content)) #['This is a text file\n', 'Hi you are good\n', 'hike kab milegi\n', 'switch kab bhai'] <class 'list'>

#readline() to read lines one by one

line = f.readline()
# print(line)
while(line != ""):
    print(line,type(f.readline()))
    line = f.readline()