word = "codeforces"
char = list(word)
t = int(input())
for _ in range(t):
    c = input()
    if c in char:
        print("YES")
    else:
        print("NO")