"""
UNFINISHED, DOES NOT WORK
"""

file1 = open("./advent-of-code-day-5/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n\n")
ingredient_ranges = inpArr[0].split("\n")
file1.close()


total_fresh_ids = 0


ranges = []

print(ingredient_ranges)


for ing_range in ingredient_ranges:
    range_1 = ing_range.split("-")
    
    if len(ranges) > 0:
        for i in range(len(ranges)):
            #print(i)
            
            if int(range_1[0]) < int(ranges[i][0]) and int(range_1[1]) > int(ranges[i][1]):
                #print("NESTED!")
                ranges[i] = 0
            elif int(ranges[i][0]) < int(range_1[1]) and int(ranges[i][1]) < int(range_1[0]):
                #print("this range is like shifted to the right, both min and max bigger than other min and max, but max not bigger than other min")
                ranges[i][0] = range_1[1]
            elif int(ranges[i][1]) < int(range_1[0]) and int(ranges[i][0]) < int(range_1[1]):
                #print("this range is like shifted to the right, both min and max bigger than other min and max, but max not bigger than other min")
                ranges[i][1] = ing_range_arr[0]
    
    while 0 in ranges:
        ranges.remove(0)
        
    ranges.append(ing_range_arr)

for r in ranges:
    total_fresh_ids += (int(r[1]) - int(r[0]))

print(ranges)


print(total_fresh_ids)


"""
fresh_ids = []


# increment total_fresh if the available ing id is within one of the ranges
for ing_range in ingredient_ranges:
    print(ing_range)
    ing_range_arr = ing_range.split("-")
    for i in range(int(ing_range_arr[0]), int(ing_range_arr[1])+1):
        print(i)
        fresh_ids.append(i)


# remove duplicates from fresh_ids
fresh_ids = list(set(fresh_ids))


print(len(fresh_ids))
"""



















"""
total_fresh_ids = 0


mins = []
maxs = []


# increment total_fresh if the available ing id is within one of the ranges
highest = 0
lowest = 99999999999999
for ing_range in ingredient_ranges:
    print(ing_range)
    ing_range_arr = ing_range.split("-")

    if int(ing_range_arr[1]) < lowest:
        lowest = int(ing_range_arr[0])
    if int(ing_range_arr[0]) > highest:
        highest = int(ing_range_arr[1])

    mins.append(int(ing_range_arr[0]))
    maxs.append(int(ing_range_arr[1]))

    # total_fresh_ids += (int(ing_range_arr[1]) - int(ing_range_arr[0])) + 2


# something like:
# subtract highest max from lowest min to get biggest rnage
# then subtract the gaps from that number
# to find the gaps: start at the lowest max, then go to the next min that comes after that number, subtract max-min from big range number, keep doing that?????????????????????????????

mins.sort()
maxs.sort()
print(mins)
print(maxs)

for min_range in mins:
    max_range = ingredient_ranges.index()

print(highest)
print(lowest)
total_fresh_ids = highest - lowest


print(total_fresh_ids)
"""