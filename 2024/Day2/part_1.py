"""
initiate safe_report_count variable
bring in data
put into lists
for each list:
shamlessly stole the turn my list into ints from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
iterate through the numbers subbing index 1 from 0, if its negative
    then its increasing so all the rest is increasing. otherwise
    they should all result in postive results. so there'll be a
    logic test AFTER the first round that goes
        if value > 0 != 0:
            its positive
        else:
            its negative
    then have a boolean to check if its consistent, if not set
    the "add_one_to_count" to False then break out of the loop
    the results shoudl be like abs(x) <= 2 != 0, to show its increasing or decreasing
        if not, break out of the loop

    or have a logic test of if sort(report) == report or sort(report, reverse) == report:
    this will check if in order already one way or anohter?
"""

safe_report_count = 0

input_file = open(r'example_input')
input_data = input_file.readlines()
for line in input_data:
    increment_report_counter = True
    report = [int(x) for x in line.split()]
    sorted_report = sorted(report)
    reverse_sorted_report = sorted(report, reverse=True)
    print(report)
    print(f'here is the sorted report {sorted_report}')
    print(f'here is the reverse sorted report {reverse_sorted_report}')
    if reverse_sorted_report == report:
        print("its reversed!")
    elif sorted_report == report:
        print("its in order!")
    else:
        print("its junk!")
        break
    length_of_report = len(report)
    print(f"there are {length_of_report} numbers in the report")
    index_tracker = 0
    for index, number in enumerate(report):
        subtracting_index = index + 1
        if subtracting_index == length_of_report:
            break
        print(f'this is index {index} this is subtracting index {subtracting_index}')
        difference = report[index] - report[subtracting_index]
        print(f'the difference of {report[index]} and {report[subtracting_index]} is equal to {difference}')
        """index_tracker += 1
        difference = number - report[1]
        print(f"the difference in {number} and {report[1]} is {difference}")
        if abs(difference) > 2 ==0:
            increment_report_counter = False
            break
        if index_tracker >= length_of_report:
            break"""
