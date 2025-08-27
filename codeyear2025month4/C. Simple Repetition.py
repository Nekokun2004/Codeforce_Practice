import math
 
def runcase():
    n, k = map(int, input().split())
    
    if n == 1:
        n = 0
        for i in range(k):
            n = n * 10 + 1
        k = 1
    
    if k > 1 or n < 2:
        print("NO")
        return
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("NO")
            return
    
    print("YES")
 
t = int(input())
for i in range(t):
    runcase()