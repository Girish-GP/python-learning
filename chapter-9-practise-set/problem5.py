# repeat problem 4 with list of words to be censored

censored_list = ['same','repeating']
contents = ""

# Read the file contents
with open("problem5.txt") as f:
    contents = f.read()

# Replace the censored words from the file content
for item in censored_list:
    contents = contents.replace(item,"#"*len(item))

# Write the censored content to the file
with open("problem5.txt","w") as f:
    f.write(contents)

