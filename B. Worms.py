import bisect

n = int(input())
lstworm = list(map(int,input().split()))
wormm = int(input())
listwormm = list(map(int,input().split()))
count = 0
index = 0
lst = []
for i in range(n):
  count += lstworm[i]
  lst.append(count)
print(lst)
while index < wormm:
  idx = bisect.bisect_right(lst, listwormm[index]) 
  if idx < len(lst) and lst[idx] != listwormm[index]:
    idx += 1
  index += 1
  print(idx)


# import sys
# import bisect

# def main():
#     data = sys.stdin.read().split()
#     it = iter(data)
    
#     n = int(next(it))
#     a = [int(next(it)) for _ in range(n)]
    
#     prefix = [0] * n
#     prefix[0] = a[0]
#     for i in range(1, n):
#         prefix[i] = prefix[i-1] + a[i]
#     print(prefix)
#     m = int(next(it))
#     out = []
#     for _ in range(m):
#         q = int(next(it))
#         pile_idx = bisect.bisect_left(prefix, q)
#         out.append(str(pile_idx + 1))
    
#     sys.stdout.write("\n".join(out))

# if __name__ == "__main__":
#     main()
