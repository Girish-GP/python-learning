# A spam comment is defined as a text conatining followinng keywords: "Make a lot of money" , "buy now", "subscribe this", "click this". Write a program to detect this spams

spamList = ["Make a lot of money" , "buy now", "subscribe this", "click this"]

text = input("Enter the text:")
isSpam = False
for item in spamList:
    # if(text.lower().find(item.lower()) != -1):
    if item.lower() in text.lower():
        isSpam = True
        break
if(isSpam):
    print(f"The text '{text}' is spam")    
else:
    print(f"The text '{text}' is not spam")            