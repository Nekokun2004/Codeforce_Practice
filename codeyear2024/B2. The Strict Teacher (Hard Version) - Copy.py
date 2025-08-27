def solve():
    import sys
    input = sys.stdin.read
    from bisect import bisect_left, bisect_right
    
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        m = int(data[index + 1])
        q = int(data[index + 2])
        index += 3
        
        pos = set()
        for _ in range(m):
            pos.add(int(data[index]))
            index += 1
        
        sorted_pos = sorted(pos)
        
        queries = []
        for _ in range(q):
            queries.append(int(data[index]))
            index += 1
        
        for a in queries:
            l_index = bisect_left(sorted_pos, a) - 1
            l = sorted_pos[l_index] if l_index >= 0 else -1
            r_index = bisect_right(sorted_pos, a)
            r = sorted_pos[r_index] if r_index < len(sorted_pos) else -1
            
            if l != -1 and r != -1:
                ans = (a - l - 1) // 2 + (r - a - 1) // 2 + 1
                if (a - l) % 2 == 0 and (r - a) % 2 == 0:
                    ans += 1
                results.append(str(ans))
            elif l == -1:
                results.append(str(r - 1))
            else:
                results.append(str(n - l))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
