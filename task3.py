while True:
 list = input().split()

 for i in range(len(list)):
    if int(list[i]) > 150:
        continue
    if int(list[i]) > 500:
        break
    if int(list[i])%5==0:
     print(list[i])