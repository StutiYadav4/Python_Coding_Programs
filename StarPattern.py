# Print the Star Pattern

inputNum = int(input("Enter a number: "))
for ind in range(1,inputNum+1):
    print(" "*int(inputNum-ind)+"* "*ind)

