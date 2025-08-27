t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    maxfirst = max(a,b)
    maxsecond = max(c,d)
    # print(f"maxfirst = {maxfirst} , maxsecond = {maxsecond}")
    if maxfirst == max(maxfirst,maxsecond):
        if maxsecond > min(a,b):
            print("YES")
        elif maxsecond < min(a,b):B. Two Arrays And Swaps
            print("NO")
    else:
        if maxfirst > min(c,d):
            print("YES")
        elif maxfirst < min(c,d):
            print("NO")
 
