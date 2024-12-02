"""
input the list input
break into two lists
for each item in list a, check how many times in list b
multuply item in list a from the odccurance in b
add this to total



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
    occurances_of_index = list_b.count(index)
    print(f'{index} was found {occurances_of_index} time(s)')
    sum += int(index) * occurances_of_index


print(f'final total is: {sum}')
