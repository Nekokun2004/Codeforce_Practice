import sys
from collections import Counter

def can_pal_after_k_deletions(n, k, s):
    odd = sum(c % 2 for c in Counter(s).values())
    d = min(odd, k)
    odd_after = odd - d
    rem = k - d
    odd_final = odd_after + (rem & 1)
    return odd_final <= ((n - k) % 2)

def solve():
    it = iter(sys.stdin.read().strip().split())
    # print("it = ",list(it))
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        s = next(it)
        out_lines.append("YES" if can_pal_after_k_deletions(n, k, s) else "NO")
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
