with open("../input.txt", "r") as f:
    contents = f.read().splitlines()

total = 0
dic = {}
curr = ""
start = None


def adjacent(r, start_col, end_col):
    if r - 1 >= 0:
        for c in range(start_col - 1, end_col + 1):
            if c >= 0 and c < len(contents[r - 1]):
                if contents[r-1][c] == "*":
                    return (True, r-1, c)

    for c in range(start_col - 1, end_col + 1):
        if c >= 0 and c < len(contents[r]):
            if contents[r][c] == "*":
                return (True, r, c)

    if r + 1 < len(contents):
        for c in range(start_col - 1, end_col + 1):
            if c >= 0 and c < len(contents[r - 1]):
                if contents[r+1][c] == "*":
                    return (True, r+1, c)
    return (False, False)


for r, line in enumerate(contents):
    for i, char in enumerate(line):
        if char.isdigit():
            curr += char
            if start is None:
                start = i
        else:
            if curr:
                result = adjacent(r, start, i)
                if result[0]:
                    success, row, col = result
                    if (row, col) in dic:
                        dic[(row, col)].append(int(curr))
                    else:
                        dic[(row, col)] = [int(curr)]
                start = None
                curr = ""

    if curr:
        result = adjacent(r, start, i)
        if result[0]:
            success, row, col = result
            if (row, col) in dic:
                dic[(row, col)].append(int(curr))
            else:
                dic[(row, col)] = [int(curr)]
            start = None
            curr = ""

for key in dic:
    if len(dic[key]) == 2:
        total += dic[key][0] * dic[key][1]

print(total)
