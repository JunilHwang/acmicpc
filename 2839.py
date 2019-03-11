n = int(input())  # 11
n5 = int(n / 5)   # 2
n3 = 0            
rm = n % 5        # 1
while rm != 0 :
  if (rm % 3 != 0) :
    n5 -= 1
    rm += 5
  temp = int(rm / 3)
  n3 += temp
  rm -= temp * 3

if n5 < 0 : print(-1)
else : print(n5+n3)