arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
size = len(s)
idx = 0
cnt = 0
while idx < size :
  if arr.count(s[idx:idx+3]) != 0 : idx += 3
  elif arr.count(s[idx:idx+2]) != 0 : idx += 2
  else : idx += 1
  cnt += 1
print(cnt)