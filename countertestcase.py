data = """
1
1
2
1 1
2
1 2
2
2 1
2
2 2
3
1 1 1
3
1 1 2
3
1 1 3
3
1 2 1
3
1 2 2
3
1 2 3
3
1 3 1
3
1 3 2
3
1 3 3
3
2 1 1
3
2 1 2
3
2 1 3
3
2 2 1
3
2 2 2
3
2 2 3
3
2 3 1
3
2 3 2
3
2 3 3
3
3 1 1
3
3 1 2
3
3 1 3
3
3 2 1
3
3 2 2
3
3 2 3
3
3 3 1
3
3 3 2
3
3 3 3
4
1 1 1 1
4
1 1 1 2
4
1 1 1 3
4
1 1 1 4
4
1 1 2 1
4
1 1 2 2
4
1 1 2 3
4
1 1 2 4
4
1 1 3 1
4
1 1 3 2
4
1 1 3 3
4
1 1 3 4
4
1 1 4 1
4
1 1 4 2
4
1 1 4 3
4
1 1 4 4
""".strip().splitlines()

count = 0
i = 0
while i < len(data):
    n = int(data[i])
    i += 1  # move to the next line
    i += 1  # skip the line with the n numbers
    count += 1

print("จำนวน testcases:", count)
