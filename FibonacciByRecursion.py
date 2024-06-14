# Print the Fibonacci Series with the help of recursion.
# 0,1,1,2,3,5,8,13,21,.....
def fibonacci(n):
    if n == 0:
        return -1
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        lst = fibonacci(n-1)
        lst.append(lst[-1]+lst[-2])
        return lst


n = int(input("enter the number of terms :"))
print(fibonacci(n))

