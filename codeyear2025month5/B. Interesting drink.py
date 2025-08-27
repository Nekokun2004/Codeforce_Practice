import sys
import bisect

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    prices = [int(next(it)) for _ in range(n)]
    prices.sort()
    
    q = int(next(it))
    out = []
    for _ in range(q):
        m = int(next(it))
        cnt = bisect.bisect_right(prices, m)
        out.append(str(cnt))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
