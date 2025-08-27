t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    decrease_steps = sum(max(0, a[i] - b[i]) for i in range(n))
    increase_steps = sum(max(0, b[i] - a[i]) for i in range(n))

    print((decrease_steps) + 1)
