from __builtins__ import *


def enumerate(sequence):
    items = []
    for index in range(len(sequence)):
        items.append((index, sequence[index]))
    return items


def shuffled(items):
    n = len(items)
    for i in range(n - 1, 0, -1):
        j = random() * (i + 1) // 1
        items[i], items[j] = items[j], items[i]
    return items


def reset_position():
    y = get_pos_y()
    for _ in range(y):
        move(South)

    x = get_pos_x()
    for _ in range(x):
        move(West)


def initialize(movement):
    change_hat(Hats.Straw_Hat)
    reset_position()
    for _, direction in movement:
        if get_entity_type() != None:
            harvest()

        if get_ground_type() == Grounds.Grassland:
            till()

        move(direction)


def auto_unlock(iterable):
    for item in iterable:
        unlock(item)


def needs_entity():
    if can_harvest():
        return harvest()
    else:
        return get_entity_type() in [None, Entities.Dead_Pumpkin]


def needs_water(e):
    return e not in [Entities.Grass, Entities.Bush] and get_water() < 0.5
