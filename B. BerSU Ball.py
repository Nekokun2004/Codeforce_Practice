def max_dance_pairs(boys, girls):
    boys.sort()
    girls.sort()
    i, j = 0, 0
    count = 0
    while i < len(boys) and j < len(girls):
        if abs(boys[i] - girls[j]) <= 1:
            count += 1
            i += 1
            j += 1
        elif boys[i] < girls[j]:
            i += 1
        else:
            j += 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    boys = list(map(int, input().split()))
    m = int(input().strip())
    girls = list(map(int, input().split()))
    result = max_dance_pairs(boys, girls)
    print(result)
