inputStr = input("Enter the string to be searched :")
file1 = open("./3_Text_Files/A.txt", "r")
read1 = file1.read()
count = 0
for i in read1.split(" "):
    if i == inputStr:
        count += 1
print(f"The occurrence of {inputStr} is :", count)


# what if i want to move full stops by code?