s = input("enter the string 1 :")
t = input("enter the string 2 :")
if len(s) != len(t):
    print("Not isomorphic")
opDict1 = {}
flag=1
for i, j in zip(s, t):
         if i in opDict1.keys():
             if j == opDict1[i]:
                print("isomorphic")

             else:
                print("not isomorphic")

         else:
            opDict1[i] = j
            flag = 0

if flag == 0:
    print("isomorphic")

==


