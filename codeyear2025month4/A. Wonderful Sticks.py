t = int(input())  
for _ in range(t):
    Box = []
    n = int(input())
    s = list(input())
    # print(s)
    # countmore = s.count('>')
    # countlow = s.count('<')
    i = -1
    # print("s[i] = ", s[i-1])
    low, high = 1, n          
    while len(Box) < n and i > -n: 
        if s[i] == '>':
            Box.insert(0,high)
            high -= 1
        else:
            Box.insert(0,low)
            low += 1
        i -= 1
        if high == -1:
            break
    Box.insert(0,high)
    print(*Box)
