import sys
cnt = int(input())
arr = []
v = {}
sumN = 0
for _ in range(cnt) :
  i = int(sys.stdin.readline())
  arr.append(i)
  v[i] = v.get(i, 0) + 1
  sumN += i

print(round(sumN / len(arr)))
if cnt == 1 :
  print(arr[0])
  print(arr[0])
  print(0)
else :
  
  arr.sort()
  v2 = sorted(v.items(), key=lambda x: (-x[1], x[0]))
  f = v2[1][0] if v2[0][1] == v2[1][1] else v2[0][0]

  print(arr[len(arr) // 2])
  print(f)
  print(arr[-1] - arr[0])