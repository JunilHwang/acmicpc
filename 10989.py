import sys
cnt = int(sys.stdin.readline())
m = [0] * 10001
for _ in range(cnt) : m[int(sys.stdin.readline())] += 1
for v in range(10001) : print(f'{v}\n' * m[v], end='')