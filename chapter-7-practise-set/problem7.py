# write a program to print below star pattern
#   *
#  ***
# *****
# n=3
n = 3
for i in range(1,n+1):
    print(" " * (n-i),end = "") # end="" restrict the default newline added by print
    print("*" * (2*i-1))
   