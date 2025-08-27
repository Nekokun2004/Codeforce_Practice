def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sol = 0
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]  
        sol += b[i] - a[i]
    print(a,b)
    order = list(range(n))
    print(order)
    order.sort(key=lambda i: (a[i], b[i]))
    print(order)
    for _i in range(n - 1):
        i = order[_i]
        j = order[_i + 1]
        if b[i] >= a[j]:
            print(sol)
            return
    
    mn = float('inf')
    for _i in range(n - 1):
        i = order[_i]
        j = order[_i + 1]
        mn = min(a[j] - b[i], mn)
    
    # Output final result
    print(sol + 2 * mn)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()