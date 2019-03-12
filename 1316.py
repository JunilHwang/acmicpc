num = int(input())
s = []
cnt = 0
for i in range(num) :
  v = input()
  stack = []
  prev = None
  chk = True
  for c in v :
    if stack.count(c) == 0 :
      stack.append(c)
      prev = c
    elif (prev != c) :
      chk = False
      break
  if chk : cnt += 1
print(cnt)