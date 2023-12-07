path = "Day6/input.txt"

times = []
distances = []

with open(path, "r", encoding="utf-8-sig") as file:
    for line in file:
        titles, vals = line.strip().split(":")

        if titles.strip() == "Time":
            times = [int(i) for i in vals.split()]
        elif titles.strip() == "Distance":
            distances = [int(i) for i in vals.split()]

solution = 1

for i in range(len(times)):
    count = 0

    for j in range(1, times[i] + 1):
        if j * (times[i] - j) > distances[i]:
            count += 1

    solution *= count

print(solution)
