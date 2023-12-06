def get_blocks():
    seed_inputs, *blocks = open("5.in").read().split("\n\n")
    seed_inputs = list(map(int, seed_inputs.split(":")[1].strip().split()))
    seeds = []

    for i in range(0, len(seed_inputs), 2):
        seeds.append((seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]))

    return blocks, seeds

blocks, seeds = get_blocks()

for block in blocks:
    ranges = []
    converted_seeds = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    while len(seeds):
        start,end = seeds.pop()
        for dest, source, length in ranges:
            overlap_start = max(start, source) #TODO: i don't really understand the overlapping yet .... friend did this
            overlap_end = min(end, source+length)
            if overlap_start < overlap_end:
                converted_seeds.append((overlap_start - source +dest, overlap_end - source +dest))
                if overlap_start > start:
                    seeds.append((start,overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            converted_seeds.append((start,end))



    seeds = converted_seeds

print(min(seeds)[0])