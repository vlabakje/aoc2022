def rounds(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.strip():
                yield line.strip().split(" ", 1)

def score(opponent, me):
    if opponent == "A":  # Rock
        outcome = {"X": 3, "Y": 6, "Z": 0}[me]
    elif opponent == "B":  # Paper
        outcome = {"X": 0, "Y": 3, "Z": 6}[me]
    elif opponent == "C":  # Scissors
        outcome = {"X": 6, "Y": 0, "Z": 3}[me]
    return outcome + {"X": 1, "Y": 2, "Z": 3}[me]

def total(filename):
    return sum(score(opponent, me) for opponent, me in rounds(filename))

print(total("example"))
print(total("input"))
