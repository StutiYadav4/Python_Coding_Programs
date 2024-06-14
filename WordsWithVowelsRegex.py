'''Find word starting with vowels
string='Errors should never pass silently. Unless explicitly silenced.'
Output: ['Errors', 'Unless', 'explicitly']'''


import re
inputStr = input("Enter a string :")
lst=[]
for i in inputStr.split(" "):
    x = re.findall("^[aeiouAEIOU]",i)
    if len(x):
        lst.append(i)
print(lst)
