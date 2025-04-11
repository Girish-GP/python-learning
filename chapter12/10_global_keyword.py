a = 89
b =10

def fun():
    global a
    a = 3
    print(a)
    print(b)

fun()
print(a)