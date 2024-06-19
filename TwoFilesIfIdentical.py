file1 = open("test1.txt", "r")
file2 = open("test2.txt", "r")
readObj1 = file1.read()
readObj2 = file2.read()
flag = 0
lst1 = []
lst2 = []
for i, j in zip(readObj1.split(), readObj2.split()):
    lst1.append(i)
    lst2.append(j)
if sorted(lst1) == sorted(lst2):
    print("True")
else:
    print("False")

