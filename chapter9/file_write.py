text = "This is to write in a file"

f = open("myTextWrite.txt","w") # create a file reference named myTextWrite.txt in write mode

f.write(text) # write the text in the file

text1 = "This is another txt"

f.write(text1)
f.write("djfksd")
f.close() # close the file