import math


file1 = open("./advent-of-code-day-2/input.txt", "r")

inp = file1.read()
inpArr = inp.split(",")
file1.close()
finalArr = []


sum = 0


for line in inpArr:
    # get the min and max of the range
    ranges = line.split("-")

    # loop through each number within the range
    for num in range(int(ranges[0]), int(ranges[1]) + 1):
        string_num = str(num)
        first_half = string_num[0 : math.floor(len(string_num) / 2)]
        second_half = string_num[math.floor(len(string_num) / 2) :]

        # if first half of number equals second half of number, add to sum
        if first_half == second_half:
            sum += num

print(sum)
