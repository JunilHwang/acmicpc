s = input()
arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt = 0
for v in s :
  size = len(arr)
  for c in range(size) :
    if arr[c].find(v) != -1 : cnt += c+3
print(cnt)