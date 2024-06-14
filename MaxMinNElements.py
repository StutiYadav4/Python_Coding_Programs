#Print max and min N elements from a tuple

inputTup = tuple(input("Enter the tuple :"))
inputNum = int(input("Enter the number :"))
lst = list(inputTup)
lst1 = sorted(lst)
lst2 = sorted(lst, reverse=True)
for ind in lst1:
    print("The minimum elements are :", lst1[0:inputNum])
    break
for ind in lst2:
    print("The maximum elements are :", lst2[0:inputNum])
    break

