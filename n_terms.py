n = int(input())
term = 2
sum = term
for i in range(2,n+1):
    term = term*10+2
    sum+=term
print(sum)
