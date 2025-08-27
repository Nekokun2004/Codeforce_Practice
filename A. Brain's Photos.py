n, m = map(int, input().split())
colorful = {'C', 'M', 'Y'}
for _ in range(n):
    if any(c in colorful for c in input().split()):
        print("#Color")
        exit()
print("#Black&White")

# n ,m = map(int,input().split())
# typecolor = True
# colorful = {'C','M','Y'}
# for i in range(n):
#   color = list(map(str,input().split()))
#   if any(c in colorful for c in color):
#     typecolor = False

# if typecolor:
#   print("#Black&White")
# else:
#   print("#Color")
