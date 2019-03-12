def d (num) :
  num = int(num)
  if num == 3 :
    arr = [
      [' ', ' ', '*', ' ', ' ', ' '],
      [' ', '*', ' ', '*', ' ', ' '],
      ['*', '*', '*', '*', '*', ' ']
    ]
    return arr
  star = d(int(num / 2))
  size = len(star)
  top = []
  btm = []
  for x in range(size) :
    space = [' '] * (num - size)
    top.append(space + star[x] + space)
  for x in range(size) :
    btm.append(star[x] + star[x])
  return top+btm

arr = d(input())
for x in arr :
  print(''.join(x))