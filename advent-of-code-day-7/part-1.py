file1 = open("./advent-of-code-day-7/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


sum = 0

# positions array keeps track of indices of current tachyon beams
positions = [inpArr[0].index("S")]

for line in inpArr:
    if "^" in line:
        # loop through each space if theres a splitter on this line
        for i in range(len(line)):
            # if current space is a splitter and its index is in positions array, its been hit
            if line[i] == "^" and i in positions:
                sum += 1
                
                # remove index of hit splitter
                positions.remove(i)
                
                # add indices of empty spaces to the left and right of hit splitter
                positions.append(i-1)
                positions.append(i+1)
                
                # remove duplicates & sort
                positions = list(set(positions))
                positions.sort()
                
                print("X", end="")
            elif line[i] == "^":
                print("^", end="")
            else:
                print(".", end="")
            
        print()

print(sum)
