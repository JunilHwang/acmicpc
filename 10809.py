s = input()
idx = [num for num in range(ord('a'), ord('z') + 1) ]
arr = ['-1'] * len(idx)
for i in range(len(s)) : 
  v = s[i]
  temp = idx.index(ord(v))
  if arr[temp] == '-1' : arr[temp] = str(i)
print(' '.join(arr))
#
# a b  c  d e  f  g  h  i j k  l  m n o  p  q  r  s  t  u  v  w  x  y  z
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 6 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1