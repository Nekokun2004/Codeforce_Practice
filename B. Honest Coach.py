for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    answer = abs(lst[1]-lst[0])
    for i in range(n-1):
        answer = min(answer,abs(lst[i+1]-lst[i]))
    print(answer)
