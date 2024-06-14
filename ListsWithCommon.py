'''Check if two lists have atleast one element in common'''

inputList1 = list(input("Enter the list 1: "))
inputList2 = list(input("Enter the list 2: "))
flag = 0
for i in inputList1:
    for j in inputList2:
        if i == j:
            flag += 1
        else:
            flag += 0
if flag >= 1:
    print("Yes, the lists have an element in common.")
else:
    print("No, the lists don't have anything in common.")


