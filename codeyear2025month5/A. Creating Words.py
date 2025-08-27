t = int(input())
for _ in range(t):
    first, second = list(input().split())
    first = list(first)
    second = list(second)
    fcopy = first[0]
    scopy = second[0]
    first[0] = scopy
    second[0] = fcopy
    print("".join(first),"".join(second))