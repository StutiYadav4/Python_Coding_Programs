nums1 = eval(input("Enter the list 1 :"))
nums2 = eval(input("Enter the list 2 :"))
opList = sorted(nums1+nums2)
m = len(opList)/2
ind1 = ind2 = int(m)
ind3 = int(m-1)
if len(opList) % 2 == 0:
    print("The median is :", (int(opList[ind1])+int(opList[ind3]))/2)
elif len(opList) %2 != 0:
    print("The median is :", opList[ind2])


# 1,2,3,4

