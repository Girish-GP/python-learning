# write a recursive function to calculate the sum of first n natural numbers

# sum(n) = n + sum(n-1)
# sum(1) = 1
# sum(2) = 1+2
# sum(3) = 1 + 2 +3
def sumOfNum(n):
    if n == 1:
      return 1
    else:
      return n + sumOfNum(n-1)

print(sumOfNum(5))
