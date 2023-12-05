def get_blocks():
    seeds, *blocks = open("5.in").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].strip().split()))
    return blocks, seeds

blocks, seeds = get_blocks()

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    converted_seeds = []
    for x in seeds:
        for dest, source, length in ranges: #is the value mapped?
            if source <= x < source + length:
                converted_seeds.append(x - source + dest) #new value
                break
        else: # no= then it keeps its
            converted_seeds.append(x)
    seeds = converted_seeds

print(min(seeds))