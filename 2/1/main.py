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

games = read_lines("input.txt")
RULE = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def set_violation(set, rule):
    for key in set:
        if rule[key] < set[key]:
            return True
    return False

def game_violation(game, rule):
    for set in game[1]:
        if set_violation(set, rule):
            return True
    return False

def filter_violations(games, rule):
    result = []
    for game in games:
        if not game_violation(game, rule):
            result.append(game)
    return result

print(sum([game[0] for game in filter_violations(games, RULE)]))
