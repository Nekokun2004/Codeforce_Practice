t = int(input())
for _ in range(t):
    n = int(input())
    r = n % 3
    if r == 0:
        print("Second")
    else:
        print("First")