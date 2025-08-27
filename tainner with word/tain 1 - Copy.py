import numpy as np

# สร้างเมทริกซ์ขนาด 4x4
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# แยกตัวประกอบเอกพจน์
U, S, V = np.linalg.svd(A)

print("U matrix:\n", U)
print("Singular values:", S)
print("V matrix:\n", V)
