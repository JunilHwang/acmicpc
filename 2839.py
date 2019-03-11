while True :
a = input()
a = int(a)
b1 = int(a / 5)
b2 = a % 5
c1 = int(a / 3)
c2 = a % 3

if b2 == 0 :
  print(b1)
elif b2 == 3 :
  print(b1 + 1)
elif c2 == 0 or (c1 > 5 and c2 == 2) :
  print(c1)
else :
  print(-1)