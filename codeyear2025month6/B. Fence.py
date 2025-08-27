import sys

def main():
    data = sys.stdin.read().split()
    n, k = map(int, data[:2])
    h = list(map(int, data[2:]))
    current_sum = sum(h[:k])
    min_sum = current_sum
    min_idx = 0 

    for i in range(1, n - k + 1):
        current_sum += h[i + k - 1] - h[i - 1]
        if current_sum < min_sum:
            min_sum = current_sum
            min_idx = i

    print(min_idx + 1)

if __name__ == "__main__":
    main()
