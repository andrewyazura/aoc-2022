with open("day-01/input.txt", "r") as file:
    sums = [
        sum([int(snack) for snack in elf.split("\n")])
        for elf in file.read().strip().split("\n\n")
    ]

print(max(sums))
print(sum(sorted(sums)[-3:]))
