operators = {'+': lambda a, b: a + b,
             '-': lambda a, b: a - b,
             '*': lambda a, b: a * b,
             '/': lambda a, b: a / b,
             }

reverse_operators = {
    ('+', True): lambda c, x: c - x,
    ('-', True): lambda c, x: c + x,
    ('*', True): lambda c, x: c / x,
    ('/', True): lambda c, x: c * x,

    ('+', False): lambda c, x: c - x,
    ('-', False): lambda c, x: x - c,
    ('*', False): lambda c, x: c / x,
    ('/', False): lambda c, x: x / c,

}


def propagate(target, known, operations):

    while target not in known:
        for _id, (a, task, b) in operations.items():
            if _id in known:
                continue

            if (a in known) and (b in known):
                aa = known[a]
                bb = known[b]
                if aa is None or bb is None:
                    v = None
                else:
                    v = operators[task](known[a], known[b])
                known[_id] = v


def solve(data):
    known = {}

    # first pass for numbers
    operations = {}
    for _id, op in data:
        if len(op.split(' ')) == 1:
            known[_id] = int(op)
        else:
            a, task, b = op.split(' ')
            new_op = (a, task, b)
            operations[_id] = new_op

    # make 'humn' None, and solve for the childs of root
    known['humn'] = None
    first, _, second = operations['root']

    propagate(first, known, operations)
    propagate(second, known, operations)

    # prepare our target
    if known[first] is None:
        target = first
        current = known[second]
    else:
        target = second
        current = known[first]

    # go down the tree using inverses
    while target != 'humn':
        a, op, b = operations[target]

        if known[a] is None:
            target = a
            current = reverse_operators[(op, True)](current, known[b])
        if known[b] is None:
            target = b
            current = reverse_operators[(op, False)](current, known[a])

    solution = int(current)
    return solution


def main():
    input_ = []
    with open('input') as in_f:
        for row in in_f:
            _id, op = row.strip().split(': ')
            input_.append((_id, op))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
