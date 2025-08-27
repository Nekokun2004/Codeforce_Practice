def solve():
    N = int(input().strip())
    A = []
    while N:
        A.append(N % 3)
        N //= 3
    print(A)
    pw = 1
    ANS = 0
    for i in range(len(A)):
        cost = 0
        cost += pw * 3
        if i >= 1:
            cost += i * (pw // 3)
        pw *= 3
        ANS += cost * A[i]

    print(ANS)


def main():
    T = int(input().strip())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
