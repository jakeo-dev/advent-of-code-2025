import re

file1 = open("./advent-of-code-day-6/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


# split input into numbers from first, second, third, fourth rows, and operations row
nums_arr_1 = inpArr[0]
nums_arr_2 = inpArr[1]
nums_arr_3 = inpArr[2]
nums_arr_4 = inpArr[3]
operations_arr = inpArr[4]


# convert string to int 
def to_int(string: str) -> int:
    if re.match(r" +", string) or string == "":
        return 0
    else:
        return int(string)


sum = 0

# set subtotal for first operation depending on operation
current_subtotal = 0
if operations_arr[0] == "+":
    current_subtotal = 0
elif operations_arr[0] == "*":
    current_subtotal = 1

current_operation = ""


# for each column, add up the nums if its +, multiply if its *, then add to sum
for i in range(0, len(operations_arr)):
    # determine current_operation based on symbol in operations_arr in current column
    if operations_arr[i] == "+" or operations_arr[i] == "*":
        current_operation = operations_arr[i]
    
    # get current number from current column
    current_num = to_int((nums_arr_1[i] + nums_arr_2[i] + nums_arr_3[i] + nums_arr_4[i]).strip())

    # if current column is a number, add/multiply current number to subtotal
    if current_num != 0:
        if current_operation == "+":
            current_subtotal += current_num
        elif current_operation == "*":
            current_subtotal *= current_num
    
    # if current column is NOT a number, add subtotal to sum
    if current_num == 0:
        sum += current_subtotal
        
        # set subtotal for next operation depending on operation
        if operations_arr[i+1] == "+":
            current_subtotal = 0
        elif operations_arr[i+1] == "*":
            current_subtotal = 1


print(sum + current_subtotal)
