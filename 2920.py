s = 0
for i in range(5) :
  num = int(input())
  if num < 40 : num = 40
  s += num
print(int(s / 5))