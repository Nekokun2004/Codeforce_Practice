import sys
rd = sys.stdin.readline

T = rd().strip()
N = len(T)

next_idx = [[-1]*26 for _ in range(N+1)]
next_idx[N] = [-1]*26
last = [-1]*26
for i in range(N-1, -1, -1):
    last = last.copy()
    last[ord(T[i]) - 97] = i
    next_idx[i] = last

chars_in_T = set(T)

Q = int(rd())
ans = []
for _ in range(Q):
    s = rd().strip()
    if any(ch not in chars_in_T for ch in s):
        ans.append("-1")
        continue

    k = len(s)
    s_idx = [ord(ch) - 97 for ch in s]
    best = None

    for start in (i for i, ch in enumerate(T) if ch == s[0]):
        p = start
        ok = True
        for j in range(1, k):
            p = next_idx[p+1][s_idx[j]]
            if p == -1:
                ok = False
                break
        if ok:
            deletions = (p - start) - (k - 1)
            if best is None or deletions < best:
                best = deletions

    ans.append(str(best if best is not None else -1))

print("\n".join(ans))
