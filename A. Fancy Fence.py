import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        a = int(data[i])
        d = 180 - a
        if d <= 0:
            ans.append("NO")
        elif 360 % d == 0 and 360 // d >= 3:
            ans.append("YES")
        else:
            ans.append("NO")
    print("\n".join(ans))

if __name__ == "__main__":
    main()
