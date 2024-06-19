#



file1 = open("./3_Text_Files/A.txt", "r")
read1 = file1.read()

file2 = open("./3_Text_Files/B.txt", "r")
read2 = file2.read()

file3 = open("./3_Text_Files/C.txt", "r")
read3 = file3.read()

file4 = open("./3_Text_Files/D.txt", "a+")
for i in (read1, read2, read3):
    print(i)
    file4.write(i)
    file4.write("\n")





