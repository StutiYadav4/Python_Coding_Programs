inputStr = input("Enter the input sentence :")
opDict = {}
for i in inputStr.split(" "):
    if i != " ":
        opDict[i] = inputStr.count(i)
print(opDict)





