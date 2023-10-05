with open("day-03/input.txt", "r") as file:
    backpacks = [bp.strip() for bp in file.readlines()]


def get_priority(char: str) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96


repeated_items = [
    get_priority(list(set(bp[: len(bp) // 2]) & set(bp[len(bp) // 2 :]))[0])
    for bp in backpacks
]

print(sum(repeated_items))

group_badges = [
    get_priority(
        list(set(backpacks[i]) & set(backpacks[i + 1]) & set(backpacks[i + 2]))[0]
    )
    for i in range(0, len(backpacks), 3)
]


print(sum(group_badges))
