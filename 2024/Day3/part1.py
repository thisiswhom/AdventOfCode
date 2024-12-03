"""`
def use_regex made with https://regex-generator.olafneumann.org/?sampleText=mul(2%2C4)&flags=im&selection=4%7CDigit,6%7CDigit`



"""
import re
final_number = 0
master_list = []

input_file = open(r'input')
input_data = input_file.readlines()

def use_regex(input_text):
    pattern = re.compile(r"mul\(\d{1,},\d{1,}\)", re.IGNORECASE)
    return pattern.findall(input_text)


for index in input_data:
    found_matches = use_regex(index)
    master_list.append(found_matches)

#master_list = master_list[0] #idk how to fix this or how I did it
for index in master_list:
    for set in index:
        matched_numbers = re.findall(r'\d{1,}', set)
        print(matched_numbers)
        number_a = int(matched_numbers[0])
        number_b = int(matched_numbers[1])
        a_times_b = number_a * number_b
        print(a_times_b)
        final_number +=a_times_b

print(final_number)





