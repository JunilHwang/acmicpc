s = input()
v1 = {'1': 0}
v2 = 0
for c in s :
  if c == '6' or c == '9' : v2 += 1
  else : v1[c] = v1.get(c, 0) + 1
m = max(list(v1.values()))
sh = int(v2 / 2)
rm = v2 % 2
print(max([m, sh + rm]))