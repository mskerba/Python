import sys
import string
import re

def filterwords(words, n):
    p = set(string.punctuation)
    words = ''.join(ch for ch in words if ch not in p)
    list = words.split()
    new_list = [item for item in list if len(item) > n]
    print(new_list)

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[2].isdigit() == 0:
        print("ERROR")
        exit(0)
    filterwords(sys.argv[1], int(sys.argv[2]))