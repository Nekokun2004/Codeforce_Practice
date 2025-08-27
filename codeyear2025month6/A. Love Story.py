t = int(input())
target = "codeforces"
for _ in range(t):
    s = input()
    diff_count = sum(1 for i in range(10) if s[i] != target[i])
    print(diff_count)
