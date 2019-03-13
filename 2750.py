cnt = int(input())
stack = [int(input()) for _ in range(cnt)]
stack.sort()
for v in stack : print(v)