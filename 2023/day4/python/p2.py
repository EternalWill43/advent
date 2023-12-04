with open("../input.txt", 'r') as f:
    contents = f.read().splitlines()

dic = {}
total = 0
for x in range(len(contents)):
    dic[x] = 1

for i, line in enumerate(contents):
    [left, right] = line.split("|")
    [_, winning] = left.split(":")
    winning = winning.strip()
    winning = [int(x) for x in winning.split(" ") if x != ""]
    numbers = [int(x) for x in right.strip().split(" ") if x != ""]
    matches = sum([1 for x in numbers if x in winning if x != ""])
    for y in range(dic[i]): 
        for x in range(matches):
            dic[x + i + 1] += 1

for x in dic:
    total += dic[x]

print(total)
