from collections import defaultdict
def get_lines():
    return open("3.in").read().strip().split('\n')
G = [[c for c in line] for line in get_lines()]
R, C = len(G), len(G[0])
p1, p2, nums = 0, 0, defaultdict(list)
for r in range(R):
    gears, n, has_part = set(), 0, False
    for c in range(C + 1):
        if c < C and G[r][c].isdigit():
            n = n * 10 + int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = G[r + rr][c + cc]
                        if not ch.isdigit() and ch != '.':
                            has_part = True
                        if ch == '*':
                            gears.add((r + rr, c + cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                p1 += n
            n, has_part, gears = 0, False, set()
print(p1)
p2 = sum(v[0] * v[1] for v in nums.values() if len(v) == 2)
print(p2)
