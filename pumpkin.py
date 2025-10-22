import utils
from __builtins__ import *


def run_pumpkin(size, movement):
    positions = set()
    for iteration in range(1000):
        for position, direction in movement:
            while position not in positions:
                if get_entity_type() != Entities.Pumpkin:
                    harvest()
                    plant(Entities.Pumpkin)
                    use_item(Items.Water)

                if can_harvest():
                    positions.add(position)
                    break

                if iteration == 0:
                    break

            if len(positions) == size * size:
                harvest()
                utils.reset_position()
                return

            move(direction)
