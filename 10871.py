s = input().split()
STR = input().split()
stack = []
for v in STR :
  if int(v) < int(s[1]) : stack.append(v)
print(' '.join(stack))