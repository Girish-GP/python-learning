try:
    a = int(input("enter a:"))
    print(a)
   
except Exception as e:
    print(f"Error: {e}")

finally: #always executes
    print("I am finally block")
    
# enter a:23
# 23
# I am finally block

# enter a:ggp
# Error : Inavlid
# I am finally block

def function1:
    try:
        a = int(input("enter a:"))
        print(a)
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    finally: #always executes
        print("I am finally block")

#in above even when we have return statement finally will execute as it bypass aby rule


def function1:
    try:
        a = int(input("enter a:"))
        print(a)
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    print("I am finally block")
    
# here last print will not excute when function is called as return is exceuted and function is stopped



