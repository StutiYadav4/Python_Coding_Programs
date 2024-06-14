#Given a text file, find all words having
#special characters and write in a separate file with two columns (word, special character)

file1 = open("test.txt", "r")
fileOut = open("output.txt", "a")
fileOut.write("word\t\tspecial character")
if not file1:
    print("ERROR IN OPENING FILE.")
else:
    readObj = file1.read()
    for i in readObj.split():
        for j in i:
            if not j.isalnum():
                fileOut.write("\n\n")
                fileOut.write(i)
                fileOut.write("\t\t")
                fileOut.write(j)
file1.close()
fileOut.close()

