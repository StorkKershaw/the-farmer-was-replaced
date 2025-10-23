import utils
from __builtins__ import *


def may_plant_companion(position, entity, companions):
    if position in companions:
        entity = companions.pop(position)

    plant(entity)

    result = get_companion()
    if result == None:
        return True

    companion, position = result
    if companion == Entities.Tree:
        return True

    companions[position] = companion
    return True


def run_companion(movement, entities, companions):
    for index, (position, direction) in utils.enumerate(movement):
        entity = entities[index % len(entities)]
        _ = (
            utils.needs_entity()
            and may_plant_companion(position, entity, companions)
            and utils.needs_water(entity)
            and use_item(Items.Water)
        )
        move(direction)
