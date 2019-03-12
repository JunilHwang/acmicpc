s = input().split(' ')
maxNum = 0
for v in s :
  v = int(v[::-1])
  if v > maxNum : maxNum = v
print(maxNum)