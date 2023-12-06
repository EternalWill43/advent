with open("../input.txt", "r") as f:
    lines = f.read().splitlines()

times = lines[0].split(":")[1].strip().split()
distances = lines[1].split(":")[1].strip().split()

speed = 1
total = 0
totals = []
for i, time in enumerate(times):
    while speed < int(time):
        distance = speed * (int(times[i]) - speed)
        if distance > int(distances[i]):
            total += 1
        speed += 1
    totals.append(total)
    total = 0
    speed = 1

ans = 1
for num in totals:
    ans *= num
print(ans)
