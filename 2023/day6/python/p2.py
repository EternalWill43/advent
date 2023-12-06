with open("../input.txt", "r") as f:
    lines = f.read().splitlines()

times = lines[0].split(":")[1].strip().split()
distances = lines[1].split(":")[1].strip().split()

time = int("".join(times))
score = int("".join(distances))
total = 0
print(time)

speed = 1
while speed < time:
    distance = speed * (time - speed)
    if distance > score:
        total += 1

    speed += 1

print(total)
