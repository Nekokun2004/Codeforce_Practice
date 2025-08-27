import math

# ฟังก์ชันหาค่า factorial (n!) หรือผลคูณของเลขทั้งหมดจาก 1 ถึง n
def factorial(n):
    if n < 0:
        return "ไม่สามารถคำนวณได้สำหรับเลขติดลบ"
    return math.factorial(n)

# ฟังก์ชันหาค่า Permutation: P(n, r) = n! / (n - r)!
# ใช้สำหรับการจัดเรียงลำดับของ r สิ่งจากทั้งหมด n สิ่ง
def permutation(n, r):
    if r > n or n < 0 or r < 0:
        return "ไม่สามารถคำนวณได้สำหรับค่าเหล่านี้"
    return math.factorial(n) // math.factorial(n - r)

# ฟังก์ชันหาค่า Combination: C(n, r) = n! / [r! * (n - r)!]
# ใช้สำหรับการเลือก r สิ่งจากทั้งหมด n สิ่ง โดยไม่สนลำดับ
def combination(n, r):
    if r > n or n < 0 or r < 0:
        return "ไม่สามารถคำนวณได้สำหรับค่าเหล่านี้"
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# พื้นที่ของสี่เหลี่ยมผืนผ้า
def area_rectangle(width, height):
    return width * height

# พื้นที่ของวงกลม
def area_circle(radius):
    return math.pi * radius**2

# พื้นที่ของสามเหลี่ยม
def area_triangle(base, height):
    return 0.5 * base * height

# พื้นที่ของสี่เหลี่ยมจัตุรัส
def area_square(side):
    return side * side

# พื้นที่ของรูปสี่เหลี่ยมขนมเปียกปูน (rhombus) ใช้ความยาวของเส้นทแยงมุม
def area_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

# พื้นที่ของรูปทรงปริซึม (trapezoid) ใช้ความยาวของฐานทั้งสองและความสูง
def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height


# ตัวอย่างการใช้งาน
n = 5
r = 3

print(f"ค่า Factorial ของ {n}: {factorial(n)}")
print(f"ค่า Permutation P({n}, {r}): {permutation(n, r)}")
print(f"ค่า Combination C({n}, {r}): {combination(n, r)}")
