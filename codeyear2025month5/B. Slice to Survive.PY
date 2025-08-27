t = int(input())
for _ in range(t):
    n,m,a,b = map(int,input().split())
    # print(n)
    count = 0
    # print("n test = ",-(-n//2))
    while n > 1 or m > 1:
        n_a = n - a
        m_b = m - b
        maxvault = max(n-a,m-b)
        if n-a > m-b:
            if m * (n-a) > (m - b) * n:
                n = a
            else:
                m = b
            count += 1
        elif m-b > n-a:
            if m * (n-a) < (m - b) * n:
                m = b
            else:
                n = a
            count += 1
        elif n-a == m-b:
            if n > m:
                n = a
                count += 1
            else:
                m = b
                count += 1
        a = -(-n//2)
        b = -(-m//2)
        print(f"n = {n},m = {m},a = {a},b = {b}")
    print(count)
