import strategy
import utils
from __builtins__ import *


def run_sunflower(size):
    clear()

    zigzag = strategy.zigzag(size, size)
    for index, (position, direction) in utils.enumerate(zigzag):
        while measure() not in {7}:
            if can_harvest():
                harvest()

            if get_ground_type() == Grounds.Grassland:
                till()

            plant(Entities.Sunflower)

            if get_water() < 0.5:
                use_item(Items.Water)

            use_item(Items.Fertilizer)
            use_item(Items.Fertilizer)

        move(direction)
        if index == 10:
            break

    directions = [
        North,
        North,
        North,
        North,
        East,
        East,
        East,
        East,
        South,
        South,
        South,
        South,
        West,
        West,
        West,
        West,
    ]

    for direction in directions:
        if get_ground_type() == Grounds.Grassland:
            till()
        move(direction)

    while True:
        for direction in directions:
            if can_harvest():
                harvest()

            if get_entity_type() != Entities.Sunflower:
                plant(Entities.Sunflower)
                if get_water() < 0.5:
                    use_item(Items.Water)

            move(direction)
