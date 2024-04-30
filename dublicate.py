list = input().split()
l1 =[]

for i in list:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')