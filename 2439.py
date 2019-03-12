n = int(input())
for v in range(n) :
  space = n - v - 1
  print((' '*space) + '*' * (v+1))