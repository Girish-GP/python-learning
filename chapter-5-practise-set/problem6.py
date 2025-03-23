# Create an empty dictionary . Allow four friends to enter their favorite language as values take their names as keys 

userInfo = {}
for i in range(1,5):
    name = input(f"Enter friend {i} name:")
    lang = input(f"Enter {name}'s favorite language:")
    userInfo[name] = lang
print(f"The final dictionary is: {userInfo}") #{'girish': 'english', 'nikhil': 'hindi', 'sharan': 'tamil', 'kaustubh': 'marathi'}


