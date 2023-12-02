with open('../input.txt', 'r') as f:
    contents = f.read()

total = 0

for line in contents.split("\n"):
    [game, gems] = line.split(":")
    gems = gems.split(";")
    game = int(game.split(" ")[1])
    blue = 0
    red = 0
    green = 0
    fail = False
    for bag in gems:
        gem_set = bag.split(",")
        for this_set in gem_set:
            this_set = this_set.strip()
            [num, color] = this_set.split(" ")
            match color:
                case "red":
                    if int(num) > red:
                        red = int(num)
                case "green":
                    if int(num) > green:
                        green = int(num)
                case "blue":
                    if int(num) > blue:
                        blue = int(num)

    total += red * green * blue

print(total)
