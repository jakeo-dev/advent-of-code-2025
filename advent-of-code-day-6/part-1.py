import re

file1 = open("./advent-of-code-day-6/input.txt", "r")

inp = file1.read()
inp = re.sub(r" +", " ", inp)
inpArr = inp.split("\n")
file1.close()


sum = 0


# split input into numbers from first, second, third, fourth rows, and operations row
nums_arr_1 = inpArr[0].strip().split(" ")
nums_arr_2 = inpArr[1].strip().split(" ")
nums_arr_3 = inpArr[2].strip().split(" ")
nums_arr_4 = inpArr[3].strip().split(" ")
operations_arr = inpArr[4].strip().split(" ")


# for each column, add up the nums if its +, multiply if its *, then add to sum
for i in range(len(operations_arr)):
    if operations_arr[i] == "+":
        sum += int(nums_arr_1[i]) + int(nums_arr_2[i]) + int(nums_arr_3[i]) + int(nums_arr_4[i])
    elif operations_arr[i] == "*":
        sum += int(nums_arr_1[i]) * int(nums_arr_2[i]) * int(nums_arr_3[i]) * int(nums_arr_4[i])


print(sum)
