st = []
for i in range(int(input())) :
  arr = input().split(' ')
  s = ''
  for v in arr[1] :
    s += v * int(arr[0])
  st.append(s)
for v in st : print(v)