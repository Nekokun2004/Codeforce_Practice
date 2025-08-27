x = [int(x) for x in input().split()]
# sumx = sum(x)
# averrage = sumx // len(x)
x.sort()
count = abs((x[1]-x[0])) + abs((x[2]-x[1]))
print(count) 