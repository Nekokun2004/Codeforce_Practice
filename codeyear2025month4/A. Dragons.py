s,n = [int(x) for x in input().split()]
Box = {}
for i in range(n):
    x,y = [int(x) for x in input().split()]
    if x not in Box:
        Box[x] = y
    else:
        Box[x] += y
Box = dict(sorted(Box.items()))
# print(Box)
# print(Box.items())
# print(list(Box.items()))
for key, data in list(Box.items()):
    if s > key:
        s += data
        del Box[key]
    else:
        print("NO")
        break
if len(Box) == 0:
    print("YES")
