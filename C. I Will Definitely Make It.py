t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    position = [(i,x) for i,x in enumerate(lst) if lst[i] > lst[k-1]]
    position = sorted(position, key=lambda x: x[1])
    # print(position)
    highwater = 0
    Drowning = False
    if len(position) > 0:
        for i,x in position:
            # print("x hereeee = ",x)
            if highwater + (x-lst[k-1]) <= lst[k-1]:
                highwater += (x-lst[k-1])
                lst[k-1] = x
            else:
                Drowning = True
                break
            # print(f" check Highwater = {highwater} and k = {lst[k-1]}")
            if x == max(position,key=lambda x:x[1]) and lst[k-1] == x:
                Drowning = False
                break
    else:
        Drowning = False
    if Drowning == True:
        print("NO")
    elif Drowning == False:
        print("YES")
