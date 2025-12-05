file1 = open("./advent-of-code-day-5/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n\n")
ingredient_ranges = inpArr[0].split("\n")
ingredients = inpArr[1].split("\n")
file1.close()


total_fresh = 0


# increment total_fresh if the available ing id is within one of the ranges
for ing_id in ingredients:
    for ing_range in ingredient_ranges:
        ing_range_arr = ing_range.split("-")

        if int(ing_id) >= int(ing_range_arr[0]) and int(ing_id) <= int(ing_range_arr[1]):
            total_fresh += 1
            break
    

print(total_fresh)
