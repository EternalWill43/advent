#FIXME: Not working on larger input

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
                dic[int(curr)] = (r, start, i)
                if adjacent(r, start, i):
                    total += int(curr)
                start = None
                curr = ""

    if curr:
        if adjacent(r, start, i):
            total += int(curr)
        curr = ""
        start = None

# for row, line in enumerate(contents):
#     for symbol_col, char in enumerate(line):
#         if not char.isdigit() and char != ".":
#             for x in dic:
#                 for col in range(dic[x][1], dic[x][2]):
#                     if (abs(dic[x][0] - row) < 2 and abs(col - symbol_col) < 2):
#                         total += x
#                         break

print(total)
