# len() --> to calculate lenght of the variable
name = "Girish"
print('Lenght of',name,'is:',len(name))

# upper() ---> to convert uppercase
print('Uppercase of',name,'is :',name.upper())

#lower() ---> to convert lowercase
print('Lowercase of',name,'is:',name.lower())

# capitalize() --> to capitalise first character
temp = 'harry'
print('Capitalise of',temp,'is :',temp.capitalize())

#title() ---> to capitalise first character of every word in a str
temp2 = 'web development'
print('Titlecase of',temp2,'is :',temp2.title())

#strip() ---> remove start and end whitespaces
temp3 = ' test name '
print('Whitespace removed of',temp3,'is :',temp3.strip())

#startsWith() and endsWith()
temp4 = 'development'
print('Whether',temp4,'starts with d ?',temp4.startswith('d'))
print('Whether',temp4,'ends with d ?',temp4.endswith('d'))

#replace()
text = "hello world"
print('Replace term world with python in',text,':',text.replace('world','python'))

# count() --> to count the number of occurrences of a substring in a string
print('Number of e in development is:',temp4.count('e')) #3

#str.find(substring)
# Returns the lowest index of the substring if found, or -1 if not found.
print('Find index of world in hello world :',text.find('world')) #6

#isdigit() --> whether string contains all digits
print('ggp'.isdigit()) #False
print('123'.isdigit()) #True

#isalpha() --> whether string contains all alphabets
print('ggp'.isalpha()) #True
print('ggp123'.isalpha()) #False

#isalnum() ---> whether string containse alphanumeric
print('hhp'.isalnum()) #True
print('hr24'.isalnum()) #True

#split() ---> 
splittext = "honey,bee"
print(splittext.split(',')) #['honey','bee'] -creates a list 