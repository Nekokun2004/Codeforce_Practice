t = int(input())
for _ in range(t):
    lst = list(input())
    Box = []
    Box2 = []
    # print(lst)
    i = 0
    while i < len(lst):
        # print("lst[i] = ",lst[i])
        if len(Box) == 0:
            Box.append(lst[i])
            Box2.append(lst[i])
            i += 1
        elif lst[i] == Box[-1] and len(Box2) != 0 and len(Box) == 1:
            Box.append(lst[i])
            i += 1
        elif lst[i] == Box[-1] and len(Box2) != 0:
            Box2.clear()
            i += 1
        elif lst[i] == Box[-1] and len(Box2) == 0:
            Box.append(lst[i])
            Box2.append(lst[i])
            i += 1
        elif lst[i] != Box[-1]:
            Box.append(lst[i])
            Box2.append(lst[i])
            i += 1
        # print("Box = ",Box)
        
    print("".join(Box))