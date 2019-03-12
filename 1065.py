def d(n) :
  cnt = 0
  last = int(n)
  for i in range(1, last + 1) :
    if i < 100 :
      cnt += 1
    else :
      s = [int(num) for num in str(i)]
      temp = []
      for n in range(len(s) - 1) :
        temp.append(s[n + 1] - s[n])
      prev = temp[0]
      chk = True
      for n in temp :
        if n != prev : chk = False; break
      if chk : cnt += 1
  print(cnt)

d(input())