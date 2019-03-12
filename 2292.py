n = int(input())
start = step = last = 1
while True :
  if n <= last : break
  last += step * 6
  step += 1
print(step)