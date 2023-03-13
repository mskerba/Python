import sys

if len(sys.argv) == 1:
    sys.exit(0)
str = ""
for i in range(len(sys.argv) - 1, 0, -1):
    if i < len(sys.argv):
        str += " "
    str += sys.argv[i].swapcase()[::-1]
print(str)

