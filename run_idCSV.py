import csv
num = input("Enter run id 1 :")
file1 = open("run_ids.csv", "r")
readObj = csv.DictReader(file1)
lst = []
for row in readObj:
    lst.append(row)
print(lst)

'''opDict={}
m = readObj.split("\n")
for i in readObj.split("\n"):
    for j in m[1:len(m)]:
        x = j.split(",")
        opDict[x[0]] = x
#print(opDict)


def chain(num):
    print(num)
    lst = opDict[num]
    if lst[-1] == '':
        if lst[1] != '':
            n = lst[1]
            opDict.get(n)
            chain(lst[1])
        else:
            print("END")
    else:
        print(lst[1])
        y = lst[-1]
        opDict.get(lst[-1])
        chain(y)


chain(num)'''





