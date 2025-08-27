import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    out.append(str((n + 1) // 2))
print("\n".join(out))
