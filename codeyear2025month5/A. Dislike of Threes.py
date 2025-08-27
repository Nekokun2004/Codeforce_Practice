import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
ks = list(map(int, data[1:]))  

max_k = max(ks)
liked = []
num = 1
while len(liked) < max_k:
    if num % 3 != 0 and num % 10 != 3:
        liked.append(num)
    num += 1

for k in ks:
    print(liked[k - 1])


# t = int(input())
# for _ in range(t):
#     k = int(input())
#     count = 0
#     num = 1
#     while True:
#         if num % 3 != 0 and num % 10 != 3:
#             count += 1
#             if count == k:
#                 print(num)
#                 break
#         num += 1
