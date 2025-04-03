textappend = "This is append text"

# f = open("file.txt","w") #if here i do write it will replace original content
f = open("file.txt","a") 

f.write(textappend)

f.close()