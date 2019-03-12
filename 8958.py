size = int(input())
quiz = []
for v in range(size) : quiz.append(input())
for v in quiz :
  score = 0
  prev = None
  num = 0
  for v2 in v :
    if v2 == 'O' :
      num += 1
      score += num
    else : num = 0
  print(score)