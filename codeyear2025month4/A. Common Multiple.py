import math

t = int(input())
for i in range(t):
    Box = []
    n = int(input())
    a = [int(x) for x in input().split()]
    new = math.lcm(*a)
    for o in a:
       Box.append(new//o)
    new = set(Box)
    print(len(new))
