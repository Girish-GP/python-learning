#what will be the length of below
s = set()
s.add(20)
s.add('20')
s.add(20.0)
print(f"Length of s is {len(s)}") #2
#20 (an integer) and 20.0 (a float) are considered the same value in Python. Even though they are of different types (int and float), they both represent the same numerical value (20). Since sets cannot have duplicates, Python treats 20 and 20.0 as a single element.