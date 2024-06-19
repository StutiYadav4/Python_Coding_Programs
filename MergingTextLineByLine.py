import os
file1 = open("./3_Text_Files/A.txt", "r")
read1 = file1.read()

file2 = open("./3_Text_Files/B.txt", "r")
read2 = file2.read()

file4 = open("./3_Text_Files/E.txt", "a")

for i, j in zip(read1.split("."), read2.split(".")):
    file4.write(i)
    file4.write(".")
    file4.write(j)




