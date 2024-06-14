# 3 4 2 7 5 8 10 6
# 3 6 1
# 8 -1 7

''' Input : arr[] = {3, 4, 2, 7, 5, 8, 10, 6}
        query indexes = {3, 6, 1}
Output: 8 -1 7
Explanation :
For the 1st query index is 3, element is 7 and
the next greater element at its right is 8
For the 2nd query index is 6, element is 10 and
there is no element greater than 10 at right,
so print -1.
For the 3rd query index is 1, element is 4 and
the next greater element at its right is 7. '''

inputList = eval(input("Enter the elements :"))
sortedList = sorted(inputList)
queryIndex = eval(input("Enter the query indexes :"))
for ind in queryIndex:
    num = inputList[int(ind)]
    '''to print next greater element'''
    for i in inputList[ind:len(inputList)]:
        if i > num:
            print(i)
            break
        elif i < num:
            continue
        elif i == sortedList[-1]:
            print("-1")





