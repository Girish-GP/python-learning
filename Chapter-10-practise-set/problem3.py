# create a class with a class attribute a . Create an object with the class and assign object.a = 0 Does this change the class attribute

class Dummy:
    a = 1

class1 = Dummy()
class1.a = 0


class2 = Dummy()
print(class1.a,class2.a) # 0 1
# Here the istance attribute a is set to 0 which does not change the class attribute