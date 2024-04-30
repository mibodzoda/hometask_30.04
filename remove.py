list = input().split()
i = 0
while i < len(list):
    if int(list[i])>50:
        del list[i]
    else:
        i += 1

print(list)