from collections import defaultdict

RESULTS = dict(win=0, draw=1, loss=2)


def invert_result(result):
    if result == 0:
        return 2
    elif result == 2:
        return 0
    return result


def parse_game(game_line):
    game = game_line.split(';')
    if len(game) == 3 and game[2] in RESULTS:
        result = RESULTS[game[2]]
        return (game[0], result), (game[1], invert_result(result))
    return []


def calculate_points(stats):
    return stats[0] * 3 + stats[1]


def format_table(results):
    table = ['Team                           | MP |  W |  D |  L |  P']

    for team, games in sorted(
            results.items(), key=lambda group: (-calculate_points(group[1]), group[0])):
        team_fmt = '{0:30} | {1:2} | {3:2} | {4:2} | {5:2} | {2:2}'
        table.append(
            team_fmt.format(team, sum(games), calculate_points(games), *games))
    return table


def tally(data):
    table = defaultdict(lambda: [0, 0, 0])

    for line in data:
        for team, result in parse_game(line):
            table[team][result] += 1

    return format_table(table)
