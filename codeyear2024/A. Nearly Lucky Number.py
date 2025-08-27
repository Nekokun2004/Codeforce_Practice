# num_input = list(input()) 
# lucky_numbers = ['4', '7'] 
# unlucky_numbers = ['0', '1', '2', '3', '5', '6', '8', '9'] 

# lucky_in_input = [num for num in num_input if num in lucky_numbers]
# unlucky_in_input = [num for num in num_input if num in unlucky_numbers]

# if len(num_input) <2 :
#     print("NO")
# elif len(unlucky_in_input) == 0 and len(lucky_in_input) > 0:  
#     print("YES")
# elif len(lucky_in_input) == 4 or len(lucky_in_input) == 7:
#     print("YES")
# else:
#     print("NO")

n = input()  # รับค่า n เป็นสตริง
lucky_digits = ['4', '7']  

# นับจำนวนตัวเลขนำโชคใน n
count_lucky_digits = sum(1 for digit in n if digit in lucky_digits)

# ตรวจสอบว่าจำนวนตัวเลขนำโชคเป็นเลขนำโชคหรือไม่
if count_lucky_digits in [4, 7]:
    print("YES")
else:
    print("NO")

