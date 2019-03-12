input()
s = [int(n) for n in input().split()]
m = max(s)
for x in range(len(s)) :
  s[x] = s[x] / m * 100
print(sum(s) / len(s))