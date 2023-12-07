path = "Day6/input.txt"

with open(path, "r", encoding="utf-8-sig") as file:
    for line in file:
        titles, vals = line.strip().split(":")

        if titles.strip() == "Time":
            time = int("".join(vals.split()))
        elif titles.strip() == "Distance":
            distance = int("".join(vals.split()))


left = 1
right = time
leftHit = False
rightHit = False

while (not leftHit) and (not rightHit):
    if left * (time - left) > distance:
        leftHit = True
    if right * (time - right) > distance:
        rightHit = True

solution = right - left + 1

print(solution)
