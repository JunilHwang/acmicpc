import sys
cnt = int(sys.stdin.readline().rstrip())
stack = [int(sys.stdin.readline().rstrip()) for _ in range(cnt)]

def d(v, size) :
  if size <= 1 : return v
  size = size // 2
  l, r = v[:size], v[size:]
  l, r = d(l, len(l)), d(r, len(r))
  len1 = len(l); len2 = len(r);
  i, j, k = 0, 0, 0
  arr = []
  while i < len1 and j < len2 :
    if l[i] < r[j] :
      arr.append(l[i]); i += 1
    else :
      arr.append(r[j]); j += 1
  if i == len1 : arr += r[j:]
  elif j == len2 : arr += l[i:]
  return arr
stack = d(stack, len(stack))
for v in stack : print(v)