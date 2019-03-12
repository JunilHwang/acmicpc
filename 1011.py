phase = int(input())
arr = []
for i in range(phase) : arr.append(input())
for v in arr :
  v = [int(n) for n in v.split()]
  r = v[1] - v[0]
  i = 1
  step = 1
  while True :
    n = i**2
    area1 = [n - i + 1, n]
    area2 = [n + 1, n + i]
    if area1[0] <= r <= area1[1] :
      print(step)
      break
    elif area2[0] <= r <= area2[1] :
      print(step + 1)
      break
    step += 2
    i += 1  