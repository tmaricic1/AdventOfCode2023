path = "Day1/input.txt"

with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

solution = 0

for line in input:
    left = 0
    right = len(line) - 1
    li = False
    ri = False
    curr = ""
    while left <= right:
        if line[left].isdigit() and not li:
            curr = line[left] + curr
            li = True
        elif not li:
            left += 1

        if line[right].isdigit() and not ri:
            curr += line[right]
            ri = True
        elif not ri:
            right -= 1

        if li and ri:
            break

    if len(curr) == 0:
        continue

    if len(curr) == 1:
        curr += curr

    solution += int(curr)

print(solution)
