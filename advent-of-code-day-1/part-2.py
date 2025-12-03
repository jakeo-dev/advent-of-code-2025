file1 = open("./advent-of-code-day-1/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


value = 50
actual_password = 0

for line in inpArr:
    direction = line[0]
    amount = int(line[1:])

    # subtract given line's amount from value if direction is left, add if right
    match direction:
        case "L":
            for i in range(amount):
                value -= 1
                
                # increment actual_password if value passes by zero
                if value % 100 == 0:
                    actual_password += 1
                    
        case "R":
            for i in range(amount):
                value += 1
                
                # increment actual_password if value passes by zero
                if value % 100 == 0:
                    actual_password += 1

    # keep adding 100 if value is below zero (range is 0-99)
    while value < 0:
        value += 100

    # keep subtracting 100 if value is above 99 (range is 0-99)
    while value > 99:
        value -= 100

print(actual_password)
