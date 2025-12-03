file1 = open("./advent-of-code-day-3/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()


total_output_joltage = 0


# get index of max number in given list
def get_max_index(list: list) -> int:
    max = -9999999999
    max_index = -1
    for i in range(len(list)):
        if int(list[i]) > max:
            max = int(list[i])
            max_index = i

    return max_index


# remove elements from start of list upto & including index
def remove_upto(list: list, index: int) -> list:
    for i in range(index + 1):
        list.pop(0)

    return list


for line in inpArr:
    # get array of batteries' joltages
    batteries = list(line)

    highests = []

    # find highest joltage excluding the last eleven
    current_highest = max(batteries[0:-11])
    current_highest_index = get_max_index(batteries[0:-11])
    batteries = remove_upto(batteries, current_highest_index)
    highests.append(current_highest)
    
    # find next highest joltages that succeed all previous joltages
    for i in range(11, 0, -1):
        current_highest = max(batteries[0 : -i + 1]) if i != 1 else max(batteries[0:])
        current_highest_index = get_max_index(batteries[0 : -i + 1]) if i != 1 else get_max_index(batteries[0:])
        if i != 1:
            batteries = remove_upto(batteries, current_highest_index)

        highests.append(current_highest)

    # combine the highest joltages into largest_joltage
    largest_joltage = int("".join(highests))

    total_output_joltage += largest_joltage

print(total_output_joltage)
