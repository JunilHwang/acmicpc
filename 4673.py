arr = [i for i in range(1, 10001)]
sn = arr[:]

def d(n) :
  total = n
  for num in str(n) : total += int(num)
  if sn.count(total) != 0 : sn.remove(total)

for i in arr : d(i)
for i in sn : print(i)