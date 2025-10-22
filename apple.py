import utils
from __builtins__ import *


def head_into_apple(x, y):
    primary = []
    secondary = []

    if get_pos_x() < x:
        primary.append(East)
        secondary.append(West)
    elif get_pos_x() > x:
        secondary.append(East)
        primary.append(West)
    else:
        secondary.append(East)
        secondary.append(West)

    if get_pos_y() < y:
        primary.append(North)
        secondary.append(South)
    elif get_pos_y() > y:
        secondary.append(North)
        primary.append(South)
    else:
        secondary.append(North)
        secondary.append(South)

    directions = utils.shuffled(primary) + utils.shuffled(secondary)
    for direction in directions:
        if move(direction):
            return True

    return False


def move_to_apple(x, y):
    while head_into_apple(x, y):
        if get_pos_x() == x and get_pos_y() == y:
            return True
    return False


def scan_apple(size):
    for row in range(size - 1):  # type: ignore
        move(North)
    move(East)

    for row in range(size // 2 - 1, -1, -1):  # type: ignore
        for col in range(size - 2):  # type: ignore
            move(East)
        move(South)

        for col in range(size - 2):  # type: ignore
            move(West)

        if row > 0:
            move(South)
        else:
            move(West)


def run_apple(size):
    max_count = size * size + 1

    change_hat(Hats.Dinosaur_Hat)
    x, y = measure()  # type: ignore
    for _ in range(max_count // 12):  # type: ignore
        if not move_to_apple(x, y):
            change_hat(Hats.Straw_Hat)
            return
        x, y = measure()  # type: ignore

    if not move_to_apple(0, 0):
        change_hat(Hats.Straw_Hat)
        return

    while get_pos_x() == 0 and get_pos_y() == 0:
        scan_apple(size)

    change_hat(Hats.Straw_Hat)
