import sys
import math

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split())
        g = math.gcd(a, b)
        dx = a // g
        dy = b // g
        if dx <= k and dy <= k:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()
