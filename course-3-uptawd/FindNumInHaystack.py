import re

handle = open('regex_sum_1941015.txt')

sum = 0
for line in handle:
    numString = re.findall('[0-9]+', line)
    if numString is not None:
        for number in numString:
            num = int(number)
            sum += num

print(sum)