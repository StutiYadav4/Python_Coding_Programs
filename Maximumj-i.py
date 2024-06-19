arr = eval(input("Enter the array :"))
max_m = 0
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if arr[i] < arr[j]:
            if j-i > max_m:
                max_m = j-i

print("The maximum is :", max_m)