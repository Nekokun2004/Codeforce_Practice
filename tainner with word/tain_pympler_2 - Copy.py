import sys
from pympler.asizeof import asizeof

# สร้างวัตถุที่ซับซ้อน
a = [1, 2, 3, {'x': 4, 'y': 5, 'z': [6, 7, 8]}, (9, 10, 11)]

# ขนาดของวัตถุโดยใช้ sys.getsizeof
size_sys = sys.getsizeof(a)
print(f"Size using sys.getsizeof: {size_sys} bytes")

# ขนาดของวัตถุโดยใช้ asizeof
size_asizeof = asizeof(a)
print(f"Size using pympler's asizeof: {size_asizeof} bytes")
