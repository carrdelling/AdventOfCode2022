
operators = {'+': lambda a, b: a+b,
             '-': lambda a, b: a-b,
             '*': lambda a, b: a*b,
             '/': lambda a, b: a/b,
             }


def solve(data):

    known = {}

    # first pass for numbers
    for _id, op in data:
        if len(op.split(' ')) == 1:
            known[_id] = int(op)

    while 'root' not in known:
        for _id, op in data:
            if _id in known:
                continue
            a, task, b = op.split(' ')
            if (a in known) and (b in known):
                v = operators[task](known[a], known[b])
                known[_id] = v

    solution = int(known['root'])
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
