''' Find the index where the left side sum is equal to right side sum

list_seq= [1,7,3,5,6]
Output:2 '''


inputList = list(input("Enter the list :"))
totalSum = 0
for i in inputList:
    totalSum += int(i)
leftSum = 0
for i, num in zip(inputList, inputList):
    totalSum -= int(num)
    leftSum += int(num)
    if leftSum == totalSum:
        print("The index of the number is :", inputList[int(i)])
        break
