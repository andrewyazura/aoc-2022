with open("day-02/input.txt", "r") as file:
    games = [game.strip().split(" ") for game in file.readlines()]

WIN = 6
TIE = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

OUTCOMES = [
    [TIE, WIN, LOSE],
    [LOSE, TIE, WIN],
    [WIN, LOSE, TIE],
]

SELECTED = [
    [SCISSORS, ROCK, PAPER],
    [ROCK, PAPER, SCISSORS],
    [PAPER, SCISSORS, ROCK],
]

scores = [OUTCOMES["ABC".index(e)]["XYZ".index(u)] + "_XYZ".index(u) for e, u in games]
adjusted_scores = [
    "XYZ".index(u) * 3 + SELECTED["ABC".index(e)]["XYZ".index(u)] for e, u in games
]

print(sum(scores))
print(sum(adjusted_scores))
