# write a program to create a dictionary of hindi words with values as their english translations . Provide the user with an option to look it up

temp = {
    'namaste':"hello",
    'kaise ho': 'how are you'
}

word = input("Enter the word you want to know meaning of:")

print(f"Meaning of {word} is {temp[word]}")