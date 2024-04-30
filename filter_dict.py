dic1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

list1 = ['A', 'C', 'F']

res = []

for i in list1:
    if i in dic1:
        res.append(dic1[i])
print(res)