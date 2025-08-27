n = int(input())

for i in range(n):
    x1,y1,x2,y2 = map(float,input().split())
    area = abs(x1-x2) * abs(y1-y2)
    print(f"Case {i+1}: {area:.2f}")