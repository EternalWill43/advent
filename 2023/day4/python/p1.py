with open("../input.txt", 'r') as f:
    contents = f.read().splitlines()

total = 0

for line in contents:
    [left, right] = line.split("|")
    [_, winning] = left.split(":")
    winning = winning.strip()
    winning = [int(x) for x in winning.split(" ")]
    numbers = [int(x) for x in right.strip().split(" ") if x != ""]
    matches = sum([1 for x in numbers if x in winning if x != ""])
    if matches > 0:
        total += pow(2, matches - 1)

print(total)

