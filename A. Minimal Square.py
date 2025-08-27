t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    option1 = max(2 * a, b) ** 2
    option2 = max(2 * b, a) ** 2
    option3 = (a + b) ** 2
    print(min(option1, option2, option3))
