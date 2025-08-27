import sys
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        k = int(data[idx]) 
        idx += 1
        first = int(data[idx]) 
        idx += 1

        cnt = 0
        for _ in range(k-1):
            x = int(data[idx])
            if x > first:
                cnt += 1
            idx += 1

        out.append(str(cnt))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()


# t = int(input())
# for i in range(t):
#     lst = list(map(int,input().split()))
#     count = 0
#     for x in lst[1:4]:
#         if x > lst[0]:
#             count += 1

#     print(count)
# # t = int(input())
# # for i in range(t):
# #     lst = list(map(int,input().split()))
# #     x = [x for x in lst if lst[0] < x]
# #     x = len(x)
# #     print(x)



