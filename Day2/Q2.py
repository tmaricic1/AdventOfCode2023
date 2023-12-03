# helper function to avoid 0s when multiplying
def non_zero(num):
    if num == 0:
        return 1
    else:
        return num


path = "Day2/input.txt"

with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

solution = 0

# for loop through each string(game)
for i in range(len(input)):
    # separate the string into a series of sets
    set_separated = input[i].split(";")

    # list of the amount of cubes played in each set(as a dictionary)
    sets = []

    # for loop through each set
    for set in set_separated:
        cubes = {"red": 0, "green": 0, "blue": 0}

        # clean up the string to get the format ['color', 'num of cubes']
        # first set will always have the game number
        if ":" in set:
            cleaned_string = set.split(":")[1].strip().replace(",", "").split()
        else:
            cleaned_string = set.strip().replace(",", "").split()

        for j in range(0, len(cleaned_string), 2):
            count = int(cleaned_string[j])
            cubes[cleaned_string[j + 1]] += count

        sets.append(cubes)

    # find the min number of cubes of each color for the set
    min_red = 0
    min_green = 0
    min_blue = 0
    for set in sets:
        min_red = max(min_red, set["red"])
        min_green = max(min_green, set["green"])
        min_blue = max(min_blue, set["blue"])

    solution += non_zero(min_red) * non_zero(min_green) * non_zero(min_blue)

print(solution)
