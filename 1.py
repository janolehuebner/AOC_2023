def get_lines():
    return open("1.in").read().strip().split('\n')
p1, p2 = 0, 0

for line in get_lines():
    p1_digits = [c for c in line if c.isdigit()]
    p2_digits = []
    for i, c in enumerate(line):
      if c.isdigit():
        p1_digits.append(c)
        p2_digits.append(c)
      for digit, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], start=1):
        if line[i:].startswith(val):
          p2_digits.append(str(digit))

    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])

print(p1)
print(p2)
