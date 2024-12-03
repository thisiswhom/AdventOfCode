import re
final_number = 0

input_file = open(r'input')
input_data = ''.join(line.strip() for line in input_file.readlines())
print(f'here is the input_data {input_data}\n and it is a {type(input_data)}')

replaced_data = re.sub(r"don't\(\).*do\(\)", "", input_data)
print(replaced_data)

found_muls = re.findall(r"mul\(\d+,\d+\)", replaced_data)
print(found_muls)


for set in found_muls:
    matched_numbers = re.findall(r'\d+', set)
    print(matched_numbers)
    number_a = int(matched_numbers[0])
    number_b = int(matched_numbers[1])
    a_times_b = number_a * number_b
    print(a_times_b)
    final_number +=a_times_b

print(final_number)