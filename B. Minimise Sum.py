

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    answer = b[0] + min(b[0],b[1])
    print(answer)
    