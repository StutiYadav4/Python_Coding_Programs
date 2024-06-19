arr = eval(input("Enter the array: "))
n = len(arr)
found = False
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i], arr[j], arr[k])
                print("******")
                found = True
if not found:
    print("No triplets found that sum to zero.")




