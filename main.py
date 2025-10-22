import cactus
import companion
import pumpkin
import strategy
import utils
from __builtins__ import *


def main():
    size = get_world_size()
    zigzag = strategy.zigzag(size, size)
    boustrophedon = strategy.boustrophedon(size, size)
    utils.initialize(zigzag)
    entities = [Entities.Sunflower, Entities.Tree, Entities.Sunflower, Entities.Carrot]
    while True:
        # companion.run_companion(zigzag, entities, {})
        # pumpkin.run_pumpkin(size, boustrophedon)
        cactus.run_cactus(size)
        utils.auto_unlock(
            [
                Unlocks.Grass,
                Unlocks.Carrots,
                Unlocks.Trees,
                Unlocks.Pumpkins,
                Unlocks.Cactus,
                Unlocks.Expand,
            ]
        )


main()
