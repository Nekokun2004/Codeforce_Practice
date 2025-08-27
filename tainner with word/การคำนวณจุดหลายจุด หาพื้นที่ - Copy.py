def polygon_area(points):
    n = len(points)
    area = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

# รับจำนวนจุดที่ต้องการ
t = int(input("Enter the number of points: "))
Box = []

# รับข้อมูลพิกัด
for _ in range(t):
    x, y = [int(x) for x in input().split()]
    Box.append((x, y))

# คำนวณพื้นที่ของรูปหลายเหลี่ยมที่สร้างจากจุดที่ป้อนมา
area = polygon_area(Box)
print(f"พื้นที่ของรูปหลายเหลี่ยม: {area:.2f}")
