# Take an array as input and remove the duplicates from the sorted array

arr = eval(input("Enter array :"))
sorted_arr = sorted(arr)
count = {}
lst = []
for i in sorted_arr:
    count[i] = 0
for i in sorted_arr:
    count[i] += 1
lst = sorted(count.keys())
print(len(lst))


