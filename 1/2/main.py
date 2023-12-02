import regex as re

def read_lines(path):
    with open(path, "r") as file:
        return file.read().strip().split("\n")

def preprocess(line: str) -> str:
    return (line.replace("one","1")
                .replace("two","2")
                .replace("three","3")
                .replace("four","4")
                .replace("five","5")
                .replace("six","6")
                .replace("seven","7")
                .replace("eight","8")
                .replace("nine","9"))

expr = "([0-9]|one|two|three|four|five|six|seven|eight|nine)"
print("regex = '%s'" % expr)
matcher = re.compile(expr)
#lines = read_lines("example.txt")
lines = read_lines("input.txt")

summa = 0
for line in lines:
    match = re.findall(matcher, line, overlapped=True)
    if match is None:
        raise Exception(line)
    groups = match
    if len(groups) == 1:
        groups.append(groups[-1])
    guess = preprocess("".join(groups[:1] + groups[-1:]))
    print("%s => %s => %s" % (line, groups, guess))
    summa += int(guess)
print(summa)
