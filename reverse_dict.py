dic1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

dic2 = dict(map(reversed,dic1.items()))

print(dic2)