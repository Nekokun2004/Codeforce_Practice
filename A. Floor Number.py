t = int(input())  
for _ in range(t):
    n, x = map(int, input().split())  
    if n <= 2:
        print(1)  
    else:
        
        floor = ((n - 2) + x - 1) // x + 1
        print(floor)