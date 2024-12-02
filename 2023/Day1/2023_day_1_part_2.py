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

- oh boy, need a new function to go through each line and replace any spelled
out number with the int version. I'm thinking some sort of list with dictionarries
with the spelled out version being the key and the actual number as the value.
that is used to iterate over the entries, when a match is found, replace the
text with the numerical version. THEN you can pass it to the find_it function

"""
import re
sum = 0

def extract_spelled_numbers(line):
    number_map = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9"
    }
    matches = []

    for word, digit in number_map.items():
        for match in re.finditer(word, line):
            start_index = match.start()
            matches.append((start_index,digit))

    for match in re.finditer('\d', line):
        start_index = match.start()
        digit = match.group()
        matches.append((start_index, digit))

    matches.sort(key=lambda x: x[0])
    found_numbers = "".join(digit for _, digit in matches)

    return found_numbers


def find_first_and_last_number(scramble):
    matches = re.findall(r'\d',scramble)
    first_digit = int(matches[0])
    last_digit = int(matches[-1])
    return first_digit * 10 + last_digit

#opens the file containing the input and creates an object
input_file = open(r"calibration_values.txt")

#reads each line and puts it in a list
list_for_summing = input_file.readlines()
print(list_for_summing)

for item in list_for_summing:
    stripped_item = item.strip()
    replaced_item = extract_spelled_numbers(stripped_item)
    calibration_result = find_first_and_last_number(replaced_item)
    print(f'the stripped item is: {stripped_item} \nthe replaces item is {replaced_item}\nthe calibration result is: {calibration_result}\n\n')
    sum += calibration_result

print(sum)