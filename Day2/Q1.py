# initialize dictionary of current cubes
loaded_cubes = {"red": 12, "green": 13, "blue": 14}

path = "Day2/input.txt"

# put the input in a list of strings
with open(path, "r", encoding="utf-8-sig") as file:
    input = [line.strip() for line in file.readlines()]

# initialize count(solution)
solution = 0

# for loop through each string(game)
for i in range(len(input)):
    # separate the string into a series of sets
    set_separated = input[i].split(";")

    game_valid = True

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

        if not (
            loaded_cubes["red"] >= cubes["red"]
            and loaded_cubes["green"] >= cubes["green"]
            and loaded_cubes["blue"] >= cubes["blue"]
        ):
            game_valid = False
            break

    if game_valid:
        solution += i + 1

print(solution)
