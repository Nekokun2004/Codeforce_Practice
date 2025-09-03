import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1+n]

    ones = sum(a)
    if ones == n:
        print(n - 1)
        return

    cur = best = 0
    for x in a:
        w = 1 if x == 0 else -1
        cur = max(w, cur + w)
        best = max(best, cur)

    print(ones + best)

if __name__ == "__main__":
    main()
