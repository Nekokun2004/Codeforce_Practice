import sys

def min_clicks(n, m):
    # If starting number is greater, only use subtract operations
    if n >= m:
        return n - m
    ops = 0
    # Greedy work backwards from m to n
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        ops += 1
    # Finally, subtract leftover difference
    return ops + (n - m)

if __name__ == "__main__":
    data = sys.stdin.read().split()
    n, m = map(int, data)
    print(min_clicks(n, m))
