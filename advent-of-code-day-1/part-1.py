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
    
    match direction:
        case "L":
            value -= amount
        case "R":
            value += amount
    
    while value < 0:
        value += 100
    while value > 99:
        value -= 100
    
    if value == 0:
        actual_password += 1

print(actual_password)