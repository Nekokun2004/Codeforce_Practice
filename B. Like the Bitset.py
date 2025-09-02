import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    integer = list(input().strip())
    ans = [x for x in range(1,n+1)]
    print(ans)
    if '0' not in integer:
        print("NO")
        continue
    positionzero = [i for i,x in enumerate(integer) if x == '0']
    print(positionzero)
    if integer[-1] != '0':
        integer[positionzero[-1]],integer[n-1] = integer[n-1],integer[positionzero[-1]]
        ans[positionzero[-1]],ans[n-1] = ans[n-1],ans[positionzero[-1]]
    print(ans)
    # for i in range(n-1,k-2,-1):
    #     print(i)
    #     print(integer[i-k+1:i+1])
        
        

        
