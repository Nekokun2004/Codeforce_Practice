import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

# step 1: เตรียม prefix array
pref = [0]*(n)
for i in range(1, n):
    pref[i] = pref[i-1] + (1 if s[i] == s[i-1] else 0)
print(pref)

# step 2: ตอบ queries
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(pref[r-1] - pref[l-1])
