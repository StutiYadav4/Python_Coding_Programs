height = list(input("Enter the heights list :"))
inFront = list(input("Enter the people in front of him taller list :"))
opList = []
# [5, 3, 2, 6, 1, 4]
# [0, 1, 2, 0, 3, 2]
# [5, 3, 2, 1, 6, 4]
def elements_greater(height,i):
    k = {}
    k[i] = 0
    for ind, i in zip(height, height):
        for j in height[0:int(height.index(ind))]:
            if ind < j:
                k[i] += 1
            else:
                k[i] += 0
    return k[i]


for i, j in zip(height, inFront):
    if elements_greater(height, i) == j:
        opList.append(i)

    '''else:
        while elements_greater(height) != j:
            m = height.index(i)
            height.insert(m-1, i)
            if elements_greater(height) == j:
                opList.append(i)
                break'''
print(opList)





