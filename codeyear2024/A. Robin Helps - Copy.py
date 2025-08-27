testcase = int(input())
for _ in range(testcase):
    money = 0
    count = 0
    n, k = map(int, input().split())
    a = list(map(int, input().split())) 
    
    for i in a:
        if i >= k:  
            money += i
        elif i == 0 and money > 0:  
            money -= 1
            count += 1
            
    print(count)
