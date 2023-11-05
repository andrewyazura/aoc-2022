with open("day-05/input.txt", "r") as file:
    string_stacks, string_commands = file.read().split("\n\n")
    string_commands = string_commands.strip()

stacks = [[] for _ in range(10)]
for line in string_stacks.split("\n")[:-1]:
    for i, c in enumerate(line[1::4]):
        if c != " ":
            stacks[i + 1].append(c)

for command in string_commands.split("\n"):
    _, ln, _, src, _, dst = command.split(" ")
    print(ln, src, dst)

    stacks[int(dst)].extend(stacks[int(src)][: -int(ln) : -1])
    stacks[int(src)][-int(ln) :] = []

print(stacks)
