t = int(input())
for i in range(t):
    n = int(input())
    a = map(int, input().split())  # ใช้ map แทนการสร้างลิสต์
    count = 0
    for j, value in enumerate(a):
        if j % 2 == 0:
            count += value
        else:
            count -= value
    print(count)
