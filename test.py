# lst = [x for x in range(1,10)]
# labels = ["Even" if x % 2 == 0 else "Odd" for x in lst]
# print(labels)

# matrix = [[i for i in range(3)] for _ in range(3)]
# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposed)

# mult_table = [[i*j for j in range(1,6)] for i in range(1,6)]
# print(mult_table)

# list1 = [1, 2]
# list2 = ['a', 'b', 'c']
# pairs = [(x, y) for x in list1 for y in list2]
# print(pairs)

# Box = {'C': 3, 'O': 2, 'D': 1, 'E': 4, 'F': 1, 'R': 5, 'S': 1}
# sortBox = sorted(Box.items(), key=lambda x:x[1] , reverse=True) #เรียงตามValues 
# sortwordBox = sorted(Box.items(), key=lambda x:x , reverse=True) #เรียงตามพยัญชนะ
# print(sortBox)
# print(sortwordBox)


# import statistics #หาฐานนิยมของช่วงlistที่ต้องการได้

# modek = statistics.mode([1, 2, 2, 3, 3])  # ❌ จะ raise StatisticsError ในบางเวอร์ชัน
# print(modek)

# from collections import Counter

# lst = [2, 3, 3, 2]
# count = Counter(lst)
# max_freq = max(count.values())

# modes = [num for num, freq in count.items() if freq == max_freq]
# print("Modes:", modes)  # Modes: [2, 3]

# from collections import Counter
# lst = [4, 4, 3, 3, 3, 3, 4, 4]
# k = 4
# num = Counter(lst)
# print(num)
# num1 = max(num.keys())
# print(num1)
# k_pos = [(i,x) for i, x in enumerate(lst) if x == k]
# print(dict(k_pos))

# lst = [x for x in range(10)]
# print(lst)
# del lst[1:5] #การลบโดยเลือก index
# print(lst)

# a = 'A' * 1337
# print(a)

#reduce(function, iterable, initializer)
#from functools import reduce
# import functools 
# import operator

# nums = [2, 3, 4]
# result0 = functools.reduce(operator.mul, nums, 1)
# result1 = functools.reduce(lambda x, y: x * y, nums, 1)

#lambda arguments: expression
# lambda x, y: x + y   # เหมือนกับฟังก์ชัน def add(x, y): return x + y

# from collections import deque

# q = deque()
# q.append(1)
# q.append(2)
# q.appendleft(0)
# print(q)  # deque([0, 1, 2])
# q.pop()     # 2
# q.popleft() # 0

# pairs = {}
# pairs[(1, 2)] = 'A'
# print(pairs[(1, 2)])  # ➜ 'A'
# print(pairs)

# d = {}
# d.setdefault('x', []).append(1)
# # d ➜ {'x':[1]}

# d = {'a':3, 'b':1, 'c':2}

# # คืน list of tuples จัดเรียงตาม value
# sorted_by_val = sorted(d.items(), key=lambda kv: kv[1])
# # ➜ [('b',1),('c',2),('a',3)]
# dictval = dict(sorted_by_val)
# # สร้าง OrderedDict ตามลำดับนั้น
# from collections import OrderedDict
# od = OrderedDict(sorted_by_val) #เป็นการคืนค่าด้วยlist แต่ใส่แปลงจากtuppleเป็นdict
# print(od) #OrderedDict({'b': 1, 'c': 2, 'a': 3}) 
# print(dictval) #{'b': 1, 'c': 2, 'a': 3}

# lst=[]
# lst.append([1 for x in range(4)])
# print(lst)


# from collections import deque
# lst = [1, 2, 3, 5, 6, 7]
# d = deque(lst)
# d.rotate(-4)  # เลขติดลบ = หมุนซ้าย / เลขบวก = หมุนขวา
# print(list(d))  # ➜ [6, 7, 1, 2, 3, 5]

# n,T = map(int,input().split())
# lst = []
# for i in range(T):
#     a,b = input().split(' ',1)
#     a = int(a)
#     lst.append((a, b)) 
# lst = sorted(lst.items() ,key=lambda x : x[1],reverse=True)
# lst.sort(reverse=True)
# print(lst)
# total = sum(map(lambda x: x[0], lst[0:3]))
# print(total)
# for i,x in lst[2::-1]:
#     print(x)


