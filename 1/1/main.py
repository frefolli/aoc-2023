import re

def read_lines():
    with open("input.txt", "r") as file:
        return file.read().strip().split("\n")


matcher_a = re.compile("^[^0-9]*([0-9]).*([0-9])[^0-9]*$")
matcher_b = re.compile("^[^0-9]*([0-9])[^0-9]*$")
lines = read_lines()
summa = 0
for line in lines:
    match = re.match(matcher_a, line)
    if match is None:
        match = re.match(matcher_b, line)
    if match is None:
        raise Exception(line)
    groups = list(match.groups())
    if len(groups) == 1:
        groups.append(groups[-1])
    summa += int("".join(groups))
print(summa)
