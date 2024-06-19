n = int(input("Enter the number of key value pairs: "))
inputDict = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    inputDict[key] = value
print(inputDict)
inputKV = input("Enter 0 for key sort or 1 for value sort :")
if inputKV != '0' and inputKV != '1':
    print("Invalid choice.")
if inputKV == '0':
    print(dict(sorted(inputDict.items())))
'''elif inputKV == '1':
    print(dict(sorted(inputDict.items() )))'''







