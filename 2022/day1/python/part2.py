with open("../input.txt", 'r') as f:
    contents = f.read()

contents = contents.split("\n\n")
arr = [sum([int(x) for x in l.split("\n")]) for l in contents]
arr.sort(reverse=True)
print(sum(arr[:3]))
