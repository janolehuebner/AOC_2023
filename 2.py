from collections import defaultdict
def get_lines():
  return open("2.in").read().strip().split('\n')
p1, p2 = 0, 0
for line in get_lines():
  ok = True
  id_, line = line.split(':')
  V = defaultdict(int)
  for event in line.split(';'):
    for balls in event.split(','):
      n,color = balls.split()
      n = int(n)
      V[color] = max(V[color], n)
      if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
        ok = False
  score = 1
  for v in V.values():
    score *= v
  p2 += score
  if ok:
    p1 += int(id_.split()[-1])
print(p1)
print(p2)