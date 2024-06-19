lst = list(input("Enter the elements :"))
for i in lst:
    if i == '0':
        lst.remove(i)
        lst.append(i)
    elif i != '0':
        continue
print(lst)