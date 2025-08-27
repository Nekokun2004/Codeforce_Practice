def fucn1(lst1):
    bitonecount = 0
    Box = []
    for i in lst1:
        x = bin(i)[2:]
        Box.append(x)
        bitonecount += x.count('1')
    return Box , bitonecount

def fucn2(lst,n,k):
    index = 0
    while k > 0 and index < n:
        binary_str = bin(lst[index])[2:]  
        if '0' in binary_str:  
            lst[index] += 1  
            k -= 1
        else:
            index += 1

    return lst , k

def fucn3(lst, k, Box, n):
    if k > 0 and all('0' not in s for s in Box):
        lst[0] += k
        k = 0
    return lst , k



t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst,k = fucn2(lst,n,k)
    print(lst)

    #finally
    Box,bitonecount= fucn1(lst)
    while k > 0:   
        lst, k = fucn3(lst, k, Box, n)
    print("K = ",k)
    Box,bitonecount= fucn1(lst)
    print("Box = ",Box)
    print("bitonecount = ",bitonecount)
    print("lst = ",lst)


# import heapq

# mod = 998244353
# N = 1000010

# def lowbit(x):
#     y = (1 << 62) - 1
#     x ^= y
#     return x & -x

# def solve():
#     n, k = map(int, input().split())
#     ans = 0
#     a = [0] * (n + 1)
#     q = []
#     for i in range(1, n + 1):
#         a[i] = int(input())
#         ans += bin(a[i]).count('1')
#         heapq.heappush(q, (-lowbit(a[i]), a[i]))
#     while True:
#         if not q:  # ถ้า queue ว่างให้หยุด
#             break
#         d, x = heapq.heappop(q)
#         d = -d  # แปลงกลับเป็นค่าบวก
#         if k - d >= 0:
#             k -= d
#             x += d
#             heapq.heappush(q, (-lowbit(x), x))
#             ans += 1
#         else:
#             break
#     print(ans)

# tt = int(input())
# for _ in range(tt):
#     solve()
