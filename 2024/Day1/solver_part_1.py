"""
input the list data
break into tuples lists within lists?
subtract each other
add result to var sum
return var sum


"""
list_a = []
list_b = []
index_of_b = 0
sum = 0

input_file = open(r'input_part_1')
input_data = input_file.readlines()

for pair in input_data:
    stripped_pair = pair.strip()
    seperated_pair = stripped_pair.split("   ")
    list_a.append(int(seperated_pair[1:][0]))
    list_b.append(int(seperated_pair[:1][0]))

list_a.sort()
list_b.sort()
print(f'sorted a is {list_a}')
print(f'sorted b is {list_b}')


for index in list_a:
    difference = index - list_b[index_of_b]
    print(f'difference of {index} and {list_b[index_of_b]} is {difference}')
    index_of_b += 1
    sum += abs(difference)
    print(f'running total is: {sum}\n')

print(f'final total is: {sum}')
