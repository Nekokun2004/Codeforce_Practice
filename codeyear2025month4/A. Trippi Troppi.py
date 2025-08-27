t = int(input())
for i in range(t):
    n = [str(x) for x in input().split()]
    result = [list(word) for word in n]
    pr = (result[0][0],result[1][0],result[2][0])
    print(f"{result[0][0]}{result[1][0]}{result[2][0]}")