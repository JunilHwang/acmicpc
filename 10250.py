iterN = int(input())
for i in range(iterN) :
  v = [int(x) for x in input().split()]
  h = v[0]; w = v[1]; n = v[2]
  a = str(int((n-1) / h) + 1)
  if len(a) < 2 : a = '0'+a
  rm = n % h
  rm = str(rm) if rm != 0 else str(h)
  print(rm+a)