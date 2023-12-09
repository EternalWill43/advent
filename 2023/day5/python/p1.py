with open("../input.txt") as f:
    lines = f.read().split("\n\n")

original = lines[0].split(":")[1].split(" ")
seeds = [int(x) for x in original if x != ""]
lines.pop(0)

seeds_soil = [[int(num) for num in x.split()]
              for x in lines[0].split("\n")[1:]]
soil_fert = [[int(num) for num in x.split()] for x in lines[1].split("\n")[1:]]
fert_water = [[int(num) for num in x.split()]
              for x in lines[2].split("\n")[1:]]
water_light = [[int(num) for num in x.split()]
               for x in lines[3].split("\n")[1:]]
light_temp = [[int(num) for num in x.split()]
              for x in lines[4].split("\n")[1:]]
temp_humid = [[int(num) for num in x.split()]
              for x in lines[5].split("\n")[1:]]
humid_loc = [[int(num) for num in x.split()] for x in lines[6].split("\n")[1:]]
humid_loc.pop()

step1 = []

for seed in seeds:
    in_range = False
    for [destination, source, seed_range] in seeds_soil:
        if seed >= source and seed < source + seed_range:
            step1.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step1.append(seed)

step2 = []
for seed in step1:
    in_range = False
    for [destination, source, seed_range] in soil_fert:
        if seed >= source and seed < source + seed_range:
            step2.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step2.append(seed)

step3 = []
for seed in step2:
    in_range = False
    for [destination, source, seed_range] in fert_water:
        if seed >= source and seed < source + seed_range:
            step3.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step3.append(seed)

step4 = []
for seed in step3:
    in_range = False
    for [destination, source, seed_range] in water_light:
        if seed >= source and seed < source + seed_range:
            step4.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step4.append(seed)

step5 = []
for seed in step4:
    in_range = False
    for [destination, source, seed_range] in light_temp:
        if seed >= source and seed < source + seed_range:
            step5.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step5.append(seed)

step6 = []
for seed in step5:
    in_range = False
    for [destination, source, seed_range] in temp_humid:
        if seed >= source and seed < source + seed_range:
            step6.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step6.append(seed)

step7 = []
for seed in step6:
    in_range = False
    for [destination, source, seed_range] in humid_loc:
        if seed >= source and seed < source + seed_range:
            step7.append(destination + (abs(source - seed)))
            in_range = True

    if not in_range:
        step7.append(seed)

print(min(step7))
