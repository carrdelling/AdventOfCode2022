

def solve(flow, tunnels):

    states = [(1, "AA", 0, ("zzz",))]
    seen = {}
    best = 0

    while len(states) > 0:

        current = states.pop()
        time, where, score, opened_s = current
        opened = {x for x in opened_s}

        if seen.get((time, where), -1) >= score:
            continue
        seen[(time, where)] = score

        if time == 30:
            best = max(best, score)
            continue

        # if we open the valve here
        if flow[where] > 0 and where not in opened:

            opened.add(where)
            new_score = score + sum(flow.get(where, 0) for where in opened)
            new_state = (time + 1, where, new_score, tuple(opened))

            states.append(new_state)
            opened.discard(where)

        # if we don't open a valve here

        new_score = score + sum(flow.get(where, 0) for where in opened)
        for option in tunnels[where]:
            new_state = (time + 1, option, new_score, tuple(opened))
            states.append(new_state)

    return best


def main():

    flows = {}
    options = {}
    with open('input') as in_f:
        for row in in_f:
            chunks = row.strip().replace('Valve ', '').split(' ')
            room, rest = chunks[0], ' '.join(chunks[1:])
            chunks = rest.replace('has flow rate=', '').split(';')
            flow, rest = int(chunks[0]), chunks[1]
            tunnels = rest.replace(' tunnels lead to valves ', '').replace(' tunnel leads to valve ', '').split(', ')

            flows[room] = flow
            options[room] = tunnels

    solution = solve(flows, options)

    print(solution)


if __name__ == "__main__":

    main()

