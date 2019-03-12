n = int(input())
stack = []
for i in range(n) : stack.append([int(a) for a in input().split()[1:]])
for v in stack :
  avg = sum(v) / len(v)
  cnt = 0
  for x in v :
    if x > avg : cnt += 1
  print(format(cnt / len(v) * 100, '.3f') + '%')