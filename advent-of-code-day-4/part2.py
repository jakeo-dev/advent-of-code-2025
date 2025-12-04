file1 = open("./advent-of-code-day-4/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


sum = 0


# loop through an arbitrary number of times
for a in range(50):
    # loop through each line
    for i in range(len(inpArr)):
        # loop through each character in each line
        for j in range(len(inpArr[i])):
            surrounding_rolls = 0
            
            if inpArr[i][j] == "@":
                # check top left
                if i >= 1 and j >= 1 and inpArr[i-1][j-1] == "@":
                    surrounding_rolls += 1
                # check top mid
                if i >= 1 and inpArr[i-1][j] == "@":
                    surrounding_rolls += 1
                # check top right
                if i >= 1 and j <= len(inpArr[i])-2 and inpArr[i-1][j+1] == "@":
                    surrounding_rolls += 1
                # check left
                if j >= 1 and inpArr[i][j-1] == "@":
                    surrounding_rolls += 1
                # check top right
                if j <= len(inpArr[i])-2 and inpArr[i][j+1] == "@":
                    surrounding_rolls += 1
                # check bottom left
                if i <= len(inpArr)-2 and j >= 1 and inpArr[i+1][j-1] == "@":
                    surrounding_rolls += 1
                # check bottom mid
                if i <= len(inpArr)-2 and inpArr[i+1][j] == "@":
                    surrounding_rolls += 1
                # check bottom right
                if i <= len(inpArr)-2 and j <= len(inpArr[i])-2 and inpArr[i+1][j+1] == "@":
                    surrounding_rolls += 1
                
                # increment sum if theres less than 4 surrounding rolls
                if surrounding_rolls < 4:
                    sum += 1
                    inpArr[i] = inpArr[i][:j] + "." + inpArr[i][j+1:]
                

# loop through each line
for i in range(len(inpArr)):
    # loop through each character in each line
    for j in range(len(inpArr[i])):
        print(inpArr[i][j], end="")
    print("\n")
        

print(sum)
