string = input("Enter the string :")
pattern = input("Enter the pattern :")
len_string = len(string)
len_pattern = len(pattern)
flag=0
for i,j in zip(pattern,string):
    if i == j:
        len_string-=1
        len_pattern-=1
    if i == ".":
        if len_string==1:
            flag+=1
    if i=="*":
        if len_string>0:
            flag+=1
            continue
if flag>0:
    print("true")
else:
    print("false")


# dynamic programming how?