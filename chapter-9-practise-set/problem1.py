# write a read the text from a given file poem.txt and find out whether it contaisn the word twinkle

with open("poem.txt") as f:
    content = f.read()
    print(content)
    if content.find('twinkle') != -1:
        print("The word twinkle is present in the file")
    else:
        print("The word twinkle is not present in file")