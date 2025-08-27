n = int(input())
count = 0
for i in range(n):
    a,b,c = [int(x) for x in input().split()]
    if a+b+c >= 2 :
        count += 1
print(count)