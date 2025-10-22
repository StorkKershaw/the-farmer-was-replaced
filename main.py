import apple
import cactus
import companion
import pumpkin
import strategy
import sunflower
import utils
from __builtins__ import *


def main():
    size = get_world_size()
    zigzag = strategy.zigzag(size, size)
    boustrophedon = strategy.boustrophedon(size, size)
    # utils.initialize(zigzag)
    entities = [Entities.Carrot]
    while True:
        # apple.run_apple(size)
        # companion.run_companion(zigzag, entities, {}, set())
        # pumpkin.run_pumpkin(size, boustrophedon)
        # cactus.run_cactus(size)
        sunflower.run_sunflower(size)
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
