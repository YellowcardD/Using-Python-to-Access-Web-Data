import re

test_filename = 'regex_sum_130354.txt'
test_file = open(test_filename)

sum_num = 0 # sum of numbers
for line in test_file:
    integers = re.findall('[0-9]+', line)
    integers = list(map(int, integers)) # convert str to int
    if len(integers) < 1: # no numbers in this line
        continue
    sum_num = sum_num + sum(integers)

print(sum_num)