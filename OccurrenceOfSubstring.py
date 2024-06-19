inputStr = input("Enter the input string :")
subString = input("Enter the substring :")
if subString in inputStr:
    print("The first position of occurrence of the substring is :", inputStr.find(subString))
    print("The number of occurrences of the substring is :", inputStr.count(subString))

else:
    print("Substring not found.")


=====