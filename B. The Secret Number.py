t = int(input())
for _ in range(t):
    n = int(input())
    answers = []
    k = 1
    while (1 + 10**k) <= n:  
        div = 1 + 10**k
        if n % div == 0:
            x = n // div
            answers.append(x)
        k += 1
    
    if not answers:
        print(0)
    else:
        answers.sort()
        print(len(answers))
        print(*answers)
