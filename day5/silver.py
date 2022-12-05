

def solve(data, moves):

    # build the stacks
    stacks = [[] for _ in range(9)]

    # reverse !
    for d in data[::-1]:
        for i in range(9):
            if d[i] != ' ':
                stacks[i].append(d[i])

    # apply moves
    for m in moves:
        count, from_, to_ = m
        from_ -= 1
        to_ -= 1

        stacks[from_], take = stacks[from_][:-count], stacks[from_][-count:]
        stacks[to_] += take[::-1]

    solution = ''.join([s[-1] for s in stacks])

    return solution


def main():

    boxes = []
    moves = []
    with open('input') as in_f:
        for row in in_f:

            if row.startswith('['):
                b = row.strip()
                next_boxes = (b[1], b[5], b[9],
                              b[13], b[17], b[21],
                              b[25], b[29], b[33])
                boxes.append(next_boxes)

            if row.startswith('move'):
                c = [r for r in row.strip().split()]
                next_move = (int(c[1]), int(c[3]), int(c[5]))
                moves.append(next_move)
            
    solution = solve(boxes, moves)

    print(solution)


if __name__ == "__main__":

    main()
