import math
t =int(input())
for _ in range(t):
    s = int(input())
    # print(s)
    root = math.sqrt(s)
    # print(root)
    if root.is_integer():
        print(0,int(root))
    else:
        print(-1)