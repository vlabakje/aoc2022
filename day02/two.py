def rounds(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.strip():
                yield line.strip().split(" ", 1)

def score(opponent, outcome):
    if opponent == "A":  # Rock
        choice = {"X": 3, "Y": 1, "Z": 2}[outcome]
    elif opponent == "B":  # Paper
        choice = {"X": 1, "Y": 2, "Z": 3}[outcome]
    elif opponent == "C":  # Scissors
        choice = {"X": 2, "Y": 3, "Z": 1}[outcome]
    return {"X": 0, "Y": 3, "Z": 6}[outcome] + choice

def total(filename):
    return sum(score(opponent, outcome) for opponent, outcome in rounds(filename))

print(total("example"))
print(total("input"))
