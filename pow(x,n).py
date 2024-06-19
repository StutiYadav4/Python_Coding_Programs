def power(x, n):
    if x == 0:
        print("invalid")
    elif n == 0:
        return 1
    else:
        return x*power(x, n-1)


x = int("Enter the number :")
n = int(input("Enter the integer :"))
print(power(x, n))


# what if i want to take x input as either int or float both?