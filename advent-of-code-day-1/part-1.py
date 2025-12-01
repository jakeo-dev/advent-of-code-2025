file1 = open("./advent-of-code-day-1/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()
finalArr = []


value = 50
actual_password = 0

for line in inpArr:
    direction = line[0]
    amount = int(line[1:])

    # subtract given line's amount from value if direction is left, add if right
    match direction:
        case "L":
            value -= amount
        case "R":
            value += amount

    # keep adding 100 if value is below zero (range is 0-99)
    while value < 0:
        value += 100

    # keep subtracting 100 if value is above 99 (range is 0-99)
    while value > 99:
        value -= 100

    # increment actual_password when value is zero
    if value == 0:
        actual_password += 1

print(actual_password)
