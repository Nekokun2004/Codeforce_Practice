import sys

input = sys.stdin.readline

t = int(input())
out = []
for i in range(t):
    n,m = map(int,input().split())
    lstx = input().strip()
    lsts = input().strip()
    if lsts in lstx:
        out.append(0)
    else:
        count = 0
        while(True):
            count += 1
            lstx *= 2 
            # print("---------------",lstx,"--------------")
            if lsts in lstx :
              out.append(count)
              break
            if len(lstx) > len(lsts)* 2:
                out.append(-1)
                break
print("\n".join(map(str,out)))

            