t = int(input())
count = 0
for _ in range(t):
    l,r = map(int,input().split())
    if l > r:
        count += 1
    elif l < r:
        count -= 1
if count > 0:
    print("Mishka")
elif count < 0:
    print("Chris")
elif count == 0:
    print("Friendship is magic!^^")