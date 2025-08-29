import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    best_q = -1
    best_i = -1
    for i in range(1, n + 1):
        a = int(next(it)); b = int(next(it))
        if a <= 10 and b > best_q:
            best_q = b
            best_i = i
    out.append(str(best_i))

print("\n".join(out))
