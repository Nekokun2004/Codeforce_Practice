t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # print(f"a = {a} , b = {b}")
    # print(f" mina = {min(a)} , maxb = {max(b)}")
    while len(b) > 0 and  k > 0 and min(a) < max(b):
        k -= 1
        # print("k = ",k)
        position = [i for i,x in enumerate(a) if x == min(a)]
        # print(position)
        a[position[0]] = max(b)
        b.remove(max(b))
        # print(a)
    print(sum(a))

    