def count_fair_competitions(heights):
    n = len(heights)
    ascents = [0] * (n - 1)
    for i in range(n - 1):
        ascents[i] = 1 if heights[i + 1] > heights[i] else 0
    cumulative_ascents = [0] * (n - 1)
    cumulative_ascents[0] = ascents[0]
    for i in range(1, n - 1):
        cumulative_ascents[i] = cumulative_ascents[i - 1] + ascents[i]
    
    fair_count = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                ascents_count = cumulative_ascents[j - 1]
            else:
                ascents_count = cumulative_ascents[j - 1] - cumulative_ascents[i - 1]
            total_segments = j - i
            descents_count = total_segments - ascents_count
            if j == n - 1:
                reverse_ascents_count = cumulative_ascents[n - 2] - cumulative_ascents[i - 1] if i > 0 else cumulative_ascents[n - 2]
            else:
                reverse_ascents_count = cumulative_ascents[j - 1] - cumulative_ascents[i - 1] if i > 0 else cumulative_ascents[j - 1]
            reverse_total_segments = total_segments
            reverse_descents_count = reverse_total_segments - reverse_ascents_count
            if ascents_count == reverse_ascents_count and descents_count == reverse_descents_count:
                fair_count += 1
    
    return fair_count


import sys
input = sys.stdin.read
data = input().split()
    
n = int(data[0])
heights = list(map(int, data[1:]))
    
result = count_fair_competitions(heights)
print(result)
