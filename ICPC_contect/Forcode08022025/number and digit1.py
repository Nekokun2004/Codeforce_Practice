import sys

try:
    for line in sys.stdin:
      line = list(line.strip("\n-"))
    #   line.reverse()
      line = line[len(line)::-1]
      line = int(''.join(line))
      print(line)

except:
    print("overProgram")