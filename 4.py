from collections import defaultdict
def get_lines():
  return open("4.in").read().strip().split('\n')
p1 = 0
Numbers = defaultdict(int)
for i,line in enumerate(get_lines()):
  Numbers[i] += 1
  first, my_numbers = line.split('|')
  card_id, card = first.split(':')
  card_nums = [int(x) for x in card.split()]
  mynums = [int(x) for x in my_numbers.split()]
  val = len(set(card_nums) & set(mynums)) #calculate value of cards
  if val > 0:
    p1 += 2**(val-1) # 2^val-1 correct value for part1
  for j in range(val):
    Numbers[i + 1 + j] += Numbers[i]
print(p1)
print(sum(Numbers.values()))
