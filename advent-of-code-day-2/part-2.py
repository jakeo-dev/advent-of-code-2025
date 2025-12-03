import math


file1 = open("./advent-of-code-day-2/input.txt", "r")

inp = file1.read()
inpArr = inp.split(",")
file1.close()


sum = 0


for line in inpArr:
    # get the min and max of the range
    ranges = line.split("-")

    # loop through each number within the range
    for num in range(int(ranges[0]), int(ranges[1]) + 1):
        string_num = str(num)
        
        # loop through every possible length segment that could repeat (length 1 to length half of number length)
        for i in range(1, math.floor(len(string_num)/2)+1):
            segment = string_num[0:i]
            
            repeats = True
            
            # loop through every part of the number of the length of the segment to see if it repeats
            for j in range(i, len(string_num), len(segment)):
                # if theres a part thats not equal to the segment, set `repeats` to false, and exit for loop
                # now we know that this number doesnt have a repeating segment
                if segment != string_num[j:j+len(segment)]:
                    repeats = False
                    break
            
            # add to sum if `repeats` is true, and exit for loop
            if repeats:
                sum += num
                break

print(sum)