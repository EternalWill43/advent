
def process_step(seeds, ranges):
    result = []
    for seed in seeds:
        in_range = False
        for [destination, source, seed_range] in ranges:
            if source <= seed < source + seed_range:
                result.append(destination + abs(source - seed))
                in_range = True
                break
        if not in_range:
            result.append(seed)
    return result


with open("../sample.txt") as f:
    lines = f.read().split("\n\n")

original = lines[0].split(":")[1].split()
seeds = [int(x) for x in original if x]
lines.pop(0)

# List of lists for each step
steps = [[int(num) for num in x.split()]
         for line in lines for x in line.split("\n")[1:] if x]

# Process each step
for step in steps:
    seeds = process_step(seeds, step)

print(min(seeds))
