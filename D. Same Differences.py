from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = defaultdict(int)
        
        for idx, val in enumerate(a, start=1):
            cnt[val - idx] += 1
        
        result = 0
        for freq in cnt.values():
            result += freq * (freq - 1) // 2
        
        print(result)

if __name__ == "__main__":
    solve()
