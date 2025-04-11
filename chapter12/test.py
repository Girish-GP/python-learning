def sum_num(*arg): #takes n number of parameters
    print(arg) # all the paramters converted into a tuple
    return sum(arg)

print(__name__) #prints "__main__" if the base file is executed and prints module name if executed from the file where the it is imported
#Test cases will only execute if the base file is executed not when it is imported in any file as a module
if __name__ == "__main__":
    print("Test 1: sum of 1,2,3,4 :",sum_num(1,2,3,4))
    print("Test 2: sum of 1,2,3,4,5 :",sum_num(1,2,3,4,5))
    print("We are directly running this code and executing the test cases.")
