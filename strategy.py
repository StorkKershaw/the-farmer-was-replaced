from __builtins__ import *


def apply(position, direction):
    x, y = position
    if direction == East:
        return x + 1, y
    if direction == West:
        return x - 1, y
    if direction == North:
        return x, y + 1
    if direction == South:
        return x, y - 1


def boustrophedon(width, height):
    patterns = [
        [
            (East, width - 1),
            (North, 1),
            (West, width - 1),
            (North, 1),
        ],
        [
            (East, width - 1),
            (North, 1),
            (West, width - 1),
        ],
        [
            (East, width - 1),
            (South, 1),
            (West, width - 1),
            (South, 1),
        ],
        [
            (East, width - 1),
            (South, 1),
            (West, width - 1),
        ],
    ]

    position = 0, 0
    movement = []

    for _ in range(height / 2 - 1):
        for direction, count in patterns[0]:
            for _ in range(count):
                movement.append((position, direction))
                position = apply(position, direction)

    for direction, count in patterns[1]:
        for _ in range(count):
            movement.append((position, direction))
            position = apply(position, direction)

    for _ in range(height / 2 - 1):
        for direction, count in patterns[2]:
            for _ in range(count):
                movement.append((position, direction))
                position = apply(position, direction)

    for direction, count in patterns[3]:
        for _ in range(count):
            movement.append((position, direction))
            position = apply(position, direction)

    return movement


def zigzag(width, height):
    pattern = [
        (East, width - 1),
        (North, 1),
        (West, width - 1),
        (North, 1),
    ]

    movement = []
    position = 0, 0

    for _ in range(height / 2):
        for direction, count in pattern:
            for _ in range(count):
                movement.append((position, direction))
                position = apply(position, direction)

    return movement
