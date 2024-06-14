''' Replace domain names of all email IDs in a list.

emails=['aa@xyz.com', 'bb@abc.com', 'cc@mnop.com']
output:['aa@gmail.com', 'bb@gmail.com', 'cc@gmail.com']'''

import re
inputStr = input("Enter the string :")
lst = inputStr.split(" ")
opList = []
for i in lst:
    x = re.sub("@[A-Za-z0-9]+\.com", "@gmail.com", i)
    opList.append(x)
print(opList)

