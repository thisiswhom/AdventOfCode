"""
- init varaible for total of items
-bring in things to be scruibebd line by line then added to a list
    - count each one, print each one, print total things imported
-take each one from the list
    - print thing we are working on
    - find the first number multiply by ten, add to terative 0
    - find the last number and add it to iterative
    - print the number
    - add to total items variable
- print new total

"""
import re
sum = \

def find_first_and_last_number(scramble):
    matches = re.findall(r'\d',scramble)
    number = int(matches[0])*10 + int(matches[-1])
    return number

#opens the file containing the data and creates an object
input_file = open(r"calibration_values.txt")

#reads each line and puts it in a list
list_for_summing = input_file.readlines()
print(list_for_summing)

for item in list_for_summing:
    #item.replace("\n", " ")
    print(f'item being checked {item} is resulted as {find_first_and_last_number(item)}')
    sum += find_first_and_last_number(item)

print(sum)