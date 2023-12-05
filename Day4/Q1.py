path = "Day4/input.txt"

# put the input in a list of strings
with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

# initialize count(solution)
solution = 0

for card in input:
    split = card.split("|")

    winningSide = split[0].split(":", 1)[-1].strip()

    winningNums = set()

    for i in winningSide.split():
        winningNums.add(i)

    count = 0

    for i in split[1].strip().split():
        if i in winningNums:
            if count == 0:
                count = 1
            else:
                count *= 2

    solution += count


print(solution)
