import re


file = "regex_sum_42.txt"
handle = open(file)
numbers = list()
sum = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)
    if len(numbers) > 0:
        for i in numbers:
            sum = sum + int(i)
print(sum)