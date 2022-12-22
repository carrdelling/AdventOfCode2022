from collections import defaultdict


def parse_pwd(chars):
    pwd = []
    buf = ''

    for c in chars:
        if c not in {'L', 'R'}:
            buf = buf + c
        else:
            n = (int(buf))
            pwd.append(n)
            pwd.append(c)
            buf = ''

    if buf != '':
        n = (int(buf))
        pwd.append(n)

    return pwd


def rotate(facing, rot):
    if rot == 'L':
        return {'>': '^', '^': '<', '<': 'v', 'v': '>'}[facing]
    if rot == 'R':
        return {'>': 'v', 'v': '<', '<': '^', '^': '>'}[facing]
    assert False, 'Bad rotate'


def rotate_score(facing):
    return {'>': 0, 'v': 1, '<': 2, '^': 3}[facing]


def draw(board, current, facing):
    screen = []

    for x in range(202):
        row = []
        for y in range(202):
            if current == (x, y):
                row.append(facing)
            else:
                row.append(board[x, y])

        screen.append(''.join(row))

    screen.append('*****')
    screen.append('*****')

    print('\n'.join(screen))


def face(current):

    xf = (current[0] - 1) // 50
    yf = (current[1] - 1) // 50

    return xf, yf


def solve(board, passwd):
    start_row = defaultdict(lambda: 99999)
    start_col = defaultdict(lambda: 99999)
    end_row = defaultdict(lambda: -99999)
    end_col = defaultdict(lambda: -99999)

    for (x, y), v in board.items():

        if v in {'.', '#'}:
            start_row[x] = min(start_row[x], y)
            end_row[x] = max(end_row[x], y)
            start_col[y] = min(start_col[y], x)
            end_col[y] = max(end_col[y], x)

    pwd = parse_pwd(passwd)

    current = (1, min(p[1] for p, v in board.items() if v != ' ' and p[0] == 1))
    current_face = face(current)
    facing = '>'

    for step in pwd:

        if step in {'L', 'R'}:
            facing = rotate(facing, step)
            continue

        steps = step

        while steps > 0:
            dx, dy = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}[facing]

            place = current[0] + dx, current[1] + dy
            status = board[place]

            if status == '.':
                current = place
                current_face = face(current)
                steps -= 1
            elif status == '#':
                steps = 0
            else:
                new_place = None
                new_facing = None
                if dx == -1:
                    ddy = 50 if (place[1] % 50) == 0 else (place[1] % 50)
                    if current_face == (2, 0):
                        new_place = 50 + ddy, 51
                        new_facing = '>'
                    elif current_face == (0, 1):
                        new_place = 150 + ddy, 1
                        new_facing = '>'
                    elif current_face == (0, 2):
                        new_place = 200, ddy
                        new_facing = '^'
                    else:
                        assert False
                elif dx == 1:
                    ddy = 50 if (place[1] % 50) == 0 else (place[1] % 50)

                    if current_face == (0, 2):
                        new_place = 50 + ddy, 100
                        new_facing = '<'
                    elif current_face == (2, 1):
                        new_place = 150 + ddy, 50
                        new_facing = '<'
                    elif current_face == (3, 0):
                        new_place = 1, 100 + ddy
                        new_facing = 'v'
                    else:
                        assert False, (current_face, current)
                elif dy == -1:
                    ddx = 50 if (place[0] % 50) == 0 else (place[0] % 50)

                    if current_face == (0, 1):
                        new_place = 151 - ddx, 1
                        new_facing = '>'
                    elif current_face == (1, 1):
                        new_place = 101, ddx
                        new_facing = 'v'
                    elif current_face == (2, 0):
                        new_place = 51 - ddx, 51
                        new_facing = '>'
                    elif current_face == (3, 0):
                        new_place = 1, 50 + ddx
                        new_facing = 'v'
                    else:
                        assert False
                elif dy == 1:
                    ddx = 50 if (place[0] % 50) == 0 else (place[0] % 50)

                    if current_face == (0, 2):
                        new_place = 151 - ddx, 100
                        new_facing = '<'
                    elif current_face == (2, 1):
                        new_place = 51 - ddx, 150
                        new_facing = '<'
                    elif current_face == (1, 1):
                        new_place = 50, 100 + ddx
                        new_facing = '^'
                    elif current_face == (3, 0):
                        new_place = 150, 50 + ddx
                        new_facing = '^'
                else:
                    assert False, 'Bad jump'

                status = board[new_place]
                if status == '.':
                    current = new_place
                    facing = new_facing
                    current_face = face(current)
                    steps -= 1
                elif status == '#':
                    steps = 0
                else:
                    assert False, ('Bad jump state', new_place)

    # final score
    solution = (current[0] * 1000) + (current[1] * 4) + rotate_score(facing)

    return solution


def main():
    board = defaultdict(lambda: ' ')
    passwd = ''
    x = 1
    with open('input') as in_f:
        for row in in_f:
            if '1' in row:
                passwd = row.strip()

            if len(row) > 0:
                for idy, c in enumerate(row.rstrip(), 1):
                    board[(x, idy)] = c
                x += 1

    solution = solve(board, passwd)

    print(solution)


if __name__ == "__main__":

    main()
