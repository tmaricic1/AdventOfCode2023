def transform(line):
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    result = ""

    i = 0
    while i < len(line):
        match = False

        for j in range(len(line), i, -1):
            curr = line[i:j]

            if curr in numbers:
                result += numbers[curr]
                i = j - 1
                match = True
                break

        if not match:
            result += line[i]
            i += 1

    return result


path = "Day1/input.txt"

with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

solution = 0

for line in input:
    line = transform(line)
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
