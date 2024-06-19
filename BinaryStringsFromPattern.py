inputStr = input("Enter the string :")


def check_(inputStr):
    for i in inputStr:
        if i == '?':
                m1 = inputStr.replace('?', '0', 1)
                m2 = inputStr.replace('?', '1', 1)
                print(m1)
                print(m2)
                check_(m1)
                check_(m2)

------