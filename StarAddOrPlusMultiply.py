numbers = "1 2 0 -1 7 9 0 2 4"

digits = list(map(int, numbers.split()))
print(digits)
firstIndex = digits[0]
expression = str(digits[0])
for i in range(1, len(digits)):
    currentNum = digits[i]
    if firstIndex > 1 and currentNum > 1:
        firstIndex *= currentNum
        expression += f" * {currentNum}"
    else:
        firstIndex += currentNum
        expression += f" + {currentNum}"

print(firstIndex)
print(expression)







