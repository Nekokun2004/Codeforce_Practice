num = int(input())
for i in range(num):
    size = input().split(" ")
    n, d, k = [int(x) for x in size]
    s_arr = [0] * (n+1)
    e_arr = [0] * (n+1)
    for j in range(k):
        job = input().split(" ")
        start, end = [int(x) for x in job]
        s_arr[start] += 1
        e_arr[end] -= 1
    current = 0
    for w in range(1,d + 1):
        current += s_arr[w]
    small_idx = 1
    small = current
    big_idx = 1
    big = current
    for w in range(1 , n-d+1):
        current += e_arr[w]
        current += s_arr[w+d]
        if current > big:
            big = current
            big_idx = w + 1
        if current < small:
            small = current
            small_idx = w + 1
        
    print(str(big_idx) + " " + str(small_idx))