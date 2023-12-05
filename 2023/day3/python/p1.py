with open("../input.txt", "r") as f:
    contents = f.read().splitlines()

total = 0
curr = ""
start = None


def adjacent(r, start_col, end_col):
    if r - 1 >= 0:
        for c in range(start_col - 1, end_col + 1):
            if c >= 0 and c < len(contents[r - 1]):
                if not contents[r-1][c].isdigit() and contents[r-1][c] != ".":
                    return True

    for c in range(start_col - 1, end_col + 1):
        if c >= 0 and c < len(contents[r]):
            if not contents[r][c].isdigit() and contents[r][c] != ".":
                return True

    if r + 1 < len(contents):
        for c in range(start_col - 1, end_col + 1):
            if c >= 0 and c < len(contents[r + 1]):
                if not contents[r+1][c].isdigit() and contents[r+1][c] != ".":
                    return True
    return False


for r, line in enumerate(contents):
    for i, char in enumerate(line):
        if char.isdigit():
            curr += char
            if start is None:
                start = i
        else:
            if curr:
                if adjacent(r, start, i):
                    total += int(curr)
                start = None
                curr = ""

    if curr:
        if adjacent(r, start, i):
            total += int(curr)
        curr = ""
        start = None


print(total)
