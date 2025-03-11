var1 = 'test' #single quoted strings
var2 = "test2" #double quoted strings
var3 = '''test3''' #triple quoted string

#String Slicing
shortVar1 = var1[0:2]
print('Sliced string is:',shortVar1)

#negative index slicing
temp = var1[-1: -3]
print('Negative sliced string is:',temp)

#lenght of variable 
x = len(var1)
print('Lenght of var1 is:',x)


temp2 = var1[:2] # start index here is 0
temp3 = var1[1:] # end index here is lenght - 1
print(temp2,temp3)

# Negative step 
name = 'Girish'
print("Negative step -1:",name[-1: -4: -1]) # hsi
print("Negative step -2:", name[-1: -4: -2]) #hi

#Positive step 
print("Postive step 1:",name[0:4:1]) #Giri
print("Positive step 2:", name[0:4:2])#Gr
print(name[0:6:3],name[0:6:2])