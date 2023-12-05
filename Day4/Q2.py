path = "Day4/input.txt"

# put the input in a list of strings
with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

cardCount = {}

# cardNum is the card number -1
for cardNum, card in enumerate(input):
    if cardNum not in cardCount:
        cardCount[cardNum] = 1

    split = card.split("|")

    winningSide = split[0].split(":", 1)[-1].strip()

    winningNums = set(winningSide.split())

    count = 0

    for i in split[1].strip().split():
        if i in winningNums:
            count += 1

    for i in range(cardNum + 1, cardNum + count + 1):
        cardCount[i] = cardCount.get(i, 1) + cardCount[cardNum]

solution = sum(cardCount.values())

print(solution)
