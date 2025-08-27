Sto = input()
n = 0

# คู่ตัวเลขที่สามารถหมุนกลับหัวแล้วตรงกัน
strobogrammatic_pairs = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6',
    '3': 'E',
    'E': '3'
}

# ตรวจสอบจากขอบซ้ายและขวาเข้าหากัน
length = len(Sto)
for i in range((length + 1) // 2):
    left_digit = Sto[i]
    right_digit = Sto[length - 1 - i]
    
    # ตรวจสอบว่าตัวเลขเป็น strobogrammatic หรือไม่
    if left_digit not in strobogrammatic_pairs or strobogrammatic_pairs[left_digit] != right_digit:
        # ถ้าตัวเลขไม่ตรงกัน ต้องนับเป็นการเปลี่ยนแปลงทั้งคู่
        n += 1

print(n)
