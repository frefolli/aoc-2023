def parse_lines(lines: list[str]) -> list:
    games = []
    for line in lines:
        game, sets = [_.strip() for _ in line.strip().split(":")]
        ID = int(game.split(" ")[1])
        content = []
        for setl in sets.split(";"):
            setc = {}
            for _ in setl.strip().split(","):
                q, c = _.strip().split(" ")
                setc[c] = int(q)
            content.append(setc)
        games.append([ID, content])
    return games

def read_lines(path: str) -> list:
    with open(path, "r") as file:
        return parse_lines(file.read().strip().split("\n"))

#games = read_lines("example.txt")
games = read_lines("input.txt")

def set_rules(set, rule):
    for key in set:
        if rule[key] < set[key]:
            rule[key] = set[key]
    return rule

def game_rules(game):
    rule = {'red': 0, 'green': 0, 'blue': 0}
    for set in game[1]:
        rule = set_rules(set, rule)
    return rule

def power(rule):
    k = 1
    for key in rule:
        k *= rule[key]
    return k

def append_rules(games):
    result = []
    for game in games:
        result.append(game + [power(game_rules(game))])
    return result

print(sum([game[2] for game in append_rules(games)]))
