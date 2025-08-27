import sys
# lines = sys.stdin.read().splitlines()
# print("sys1 = ",lines)
# print("sys2 = ",sys.stdin.read())
# print("sys3 = ",sys.stdin)
try:
    for line in sys.stdin:
        # print("line = ",line)
        word = set(list(line.strip('\n-')))
        # word = set(list(word))
        # print("word = ",word)
        print(len(word))
except:
    print("over Program")


# try:
#     for line in sys.stdin:
#       line = list(line.strip("\n-"))
#       line = sum(map(int,line))
#       print(line)

# except:
#     print("kuy sus yed mae hua door")