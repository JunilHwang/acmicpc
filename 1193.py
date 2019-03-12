n = 16
cnt = 1
r = 1
temp = False
while True :
  if n <= r :
    idx = r - n
    prefix = str(cnt - idx)
    suffix = str(idx + 1)
    if temp : print(prefix + '/' + suffix)
    else :  print(suffix + '/' + prefix)
    break;
  else :
    temp = not temp
    cnt += 1
    r += cnt