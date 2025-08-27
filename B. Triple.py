import sys
input = sys.stdin.read
print(input)
data = input().split()
print(data)
index = 0

t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    print("n here = ",n)
    index += 1

    a = list(map(int, data[index:index + n]))
    index += n
    freq = [0] * (n + 2) 

    ans = -1
    for num in a:
        freq[num] += 1
        if freq[num] == 3:
            ans = num
            break  

    results.append(str(ans))

print('\n'.join(results))
