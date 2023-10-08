with open("day-04/input.txt", "r") as file:
    pairs = [
        [[int(n) for n in r.split("-")] for r in p.strip().split(",")]
        for p in file.readlines()
    ]

containing = len(
    list(
        filter(
            lambda p: (p[0][0] <= p[1][0] <= p[1][1] <= p[0][1])
            or (p[1][0] <= p[0][0] <= p[0][1] <= p[1][1]),
            pairs,
        )
    )
)

print(containing)

overlapping = len(
    list(
        filter(
            lambda p: (p[1][0] <= p[0][1] and p[1][1] >= p[0][0])
            or (p[0][1] <= p[1][1] and p[0][1] >= p[1][0]),
            pairs,
        )
    )
)

print(overlapping)
