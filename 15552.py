import sys
num = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip().split() for i in range(num)]
for v in arr : print(int(v[0]) + int(v[1]))