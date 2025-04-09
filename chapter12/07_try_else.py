try:
    a = int(input("enter a:"))
    print(a)
   
except Exception as e:
    print(f"Error: {e}")

else: # only executes if try is successful
    print("I am else block")

# enter a:34
# 34
# I am else block

# enter a: ggp
# Error: Invalid