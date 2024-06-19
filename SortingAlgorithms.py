# Bubble Sort--increasing order--form bubbles and sort 2-2 elements compare--and keep going with the iterations.

arr = eval(input("Enter the list :"))
for j in range(len(arr)):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            continue
print(arr)


# Selection Sort

arr = eval(input("Enter the list :"))
for i in range(0, len(arr)):
    min_m = min(arr)
    arr.remove(min_m)
    arr.insert(i, min_m)
    print(arr)
arr = arr[i+1:]





