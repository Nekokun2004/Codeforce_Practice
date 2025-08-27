t = int(input())  # จำนวน test cases
test_cases = []

for _ in range(t):
    n = int(input())
    h = [list(map(int, input().split())) for _ in range(n)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, h, a, b))

for case_num, (n, h, a, b) in enumerate(test_cases, start=1):
    print(f"Test case {case_num}:")
    for i in range(n):
        for j in range(n):
            current = h[i][j]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # บน, ล่าง, ซ้าย, ขว

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    if h[ni][nj] == current:
                        print(f"  พบค่าซ้ำกันที่ h[{i}][{j}] == h[{ni}][{nj}] == {current}")
                        # เพิ่มทั้งแถว h[ni]
                        h[ni] = [x + 1 for x in h[ni]]
                        print(f"  เพิ่มค่าทั้งแถวที่ {ni} กลายเป็น {h[ni]}")
    print("ผลลัพธ์ตาราง h หลังการอัปเดต:")
    for row in h:
        print(*row)
    print()  # เว้นบรรทัดระหว่าง test case
