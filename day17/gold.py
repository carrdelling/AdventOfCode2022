

def build_shape(bottom, count):

    _type = count % 5
    x = bottom + 4

    """
    ####
    """
    if _type == 0:
        return [[x, 2], [x, 3], [x, 4], [x, 5]]

    """
    .#.
    ###
    .#.
    """
    if _type == 1:
        return [[x + 1, 2], [x + 1, 3], [x, 3], [x + 2, 3], [x + 1, 4]]

    """
    ..#
    ..#
    ###
    """
    if _type == 2:
        return [[x, 2], [x, 3], [x, 4], [x + 1, 4], [x + 2, 4]]

    """
    #
    #
    #
    #
    """
    if _type == 3:
        return [[x, 2], [x + 1, 2], [x + 2, 2], [x + 3, 2]]

    """
    ##
    ##
    """
    if _type == 4:
        return [[x, 2], [x + 1, 2], [x + 1, 3], [x, 3]]

    assert False, f"Bad tile"


def check_collision(rock, screen):

    for rx, ry in rock:
        if ((rx, ry) in screen) or (ry < 0) or (ry > 6) or (rx < 1):
            return True

    return False


def signature(screen, turn, tick):

    max_h = [0] * 7

    for rx, ry in screen:
        max_h[ry] = max(max_h[ry], rx)
    offset = min(max_h)
    top_view = tuple(x - offset for x in max_h)

    return turn % 5, tick, top_view


def solve(data):

    ins = str(data)
    tick = 0

    screen = set()
    seen = {}

    TURNS = 1000000000000
    extra_levels = 0

    turn = 0
    while turn < TURNS:

        bottom = max(x[0] for x in screen) if len(screen) > 0 else 0
        rock = build_shape(bottom, turn)
        can_fall = True

        while can_fall:

            # apply stream
            mov = ins[tick]
            tick = (tick + 1) % len(ins)

            if mov == '<':
                next_rock = [[rr[0], rr[1] - 1] for rr in rock]
            elif mov == '>':
                next_rock = [[rr[0], rr[1] + 1] for rr in rock]
            else:
                assert False, "Bad move"

            collision = check_collision(next_rock, screen)

            # apply horizontal move
            if not collision:
                rock = [x for x in next_rock]
            else:
                pass

            # apply gravity
            next_rock = [[rr[0] - 1, rr[1]] for rr in rock]

            collision = check_collision(next_rock, screen)

            if not collision:
                rock = [x for x in next_rock]
            else:
                can_fall = False
        else:
            # end of this tile
            for x in rock:
                fixed = (x[0], x[1])
                assert fixed not in screen, "Bad collision"
                screen.add(fixed)

            state = signature(screen, turn, tick)

        bottom = max(x[0] for x in screen)
        if state not in seen:
            seen[state] = turn, bottom
        else:
            # loop found
            old_turn, old_bottom = seen[state]
            growth = bottom - old_bottom
            t_diff = turn - old_turn

            cycles = (TURNS - turn) // t_diff
            extra_levels += cycles * growth
            turn += cycles * t_diff

        turn += 1

    solution = max(x[0] for x in screen) + extra_levels

    return solution


def main():

    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_ = v

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
