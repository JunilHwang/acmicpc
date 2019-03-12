s = input().lower()
vector = {}
maxNum = 0
for v in s :
  vector[v] = vector.get(v, 0) + 1
  if maxNum < vector[v] : maxNum = vector[v]
values = list(vector.values())
keys = list(vector.keys())
if values.count(maxNum) > 1 :
  print('?')
else :
  key = values.index(maxNum)
  print(keys[key].upper())