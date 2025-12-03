file1 = open("./advent-of-code-day-3/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


total_output_joltage = 0


for line in inpArr:
    # get array of batteries' joltages
    batteries = list(line)
    # find highest joltage excluding the last one
    highest_1 = max(batteries[0:-1])
    highest_1_index = batteries.index(highest_1)
    # find second highest joltage that succeeds first highest
    highest_2 = max(batteries[highest_1_index+1:])
    
    largest_joltage = int(str(highest_1) + str(highest_2))
    
    total_output_joltage += largest_joltage

print(total_output_joltage)
