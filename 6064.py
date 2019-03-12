phase = int(input())
for _ in range(phase) :
  m, n, x, y = map(int, input().split(' '))
  while x <= m*n :
    if (x-y)%n == 0 : break
    x += m
    if x % n == y : break
  if x >= m*n : x = -1
  print(x)