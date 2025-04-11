# write a display a/b where a and b are integers . if b == 0 display infinite by using ZeroDivisionError

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print("Infinite")