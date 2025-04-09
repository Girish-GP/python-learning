try:
    a = int(input("enter a number:"))
    print(a)
except ValueError as v:
    print(f"Value Error: {v}")
except Exception as e:
    print(f"Exception Error: {e}")
finally:
    print("Program finished")
    