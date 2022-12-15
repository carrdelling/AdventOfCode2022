

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(data):

    target = 2000000
    blocked = set()

    for s, b in data:
        d = distance(s, b)
        power = d - abs(s[1] - target)

        if power >= 0:
            for xx in range(-power, power+1):
                blocked.add(s[0] + xx)

    for s, b in data:
        if b[1] == target:
            blocked.discard(b[0])

    return len(blocked)


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            s, b = row.strip().replace('Sensor at ', '').replace(' closest beacon is at ', '').split(':')
            ss = tuple(int(x.split('=')[1]) for x in s.split(', '))
            bb = tuple(int(x.split('=')[1]) for x in b.split(', '))
            input_.append((ss, bb))
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
