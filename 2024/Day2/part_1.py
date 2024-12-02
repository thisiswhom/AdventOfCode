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
    for number in report:
        pass
