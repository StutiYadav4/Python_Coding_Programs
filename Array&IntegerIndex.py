arr = list(input("Enter a list: "))
inputNum = int(input("Enter a number: "))
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if int(arr[i]) + int(arr[j]) == inputNum and i !=j:
            ind1 = i
            ind2 = j
        else:
            continue
print("The index of the first element is :", ind1)
print("The index of the second element is :", ind2)




