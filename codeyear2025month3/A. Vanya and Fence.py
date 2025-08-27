a,b = [int(i) for i in input().split()]
c = [int(x) for x in input().split()]
count = 0
for i in range(a):
    if c[i] <= b:
        count += 1
    else:
        count += 2
print(count)