# 4층 1 6 21 
# 3층 1 5 15 35
# 2층 1 4 10 20
# 1층 1 3 6  10
# 0층 1 2 3  4
phase = int(input())
txt = []
for p in range(phase) :
  k = int(input())
  n = int(input())
  i = 0
  j = 0
  stack = []
  for i in range(k+1) :
    stack.append([])
    for j in range(n) :
      if j == 0 : v = 1
      elif i == 0 : v = j + 1
      elif i > 0 : v = stack[i][j-1] + stack[i-1][j]
      stack[i].append(v)
  txt.append(stack[k][n-1])
for t in txt : print(t)