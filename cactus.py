from __builtins__ import *


def run_cactus(size):
    grid = []

    def swap_prev_horizontal(r, c):
        if grid[r][c - 1] <= grid[r][c]:
            return

        grid[r][c], grid[r][c - 1] = grid[r][c - 1], grid[r][c]
        swap(West)

    def swap_next_horizontal(r, c):
        if grid[r][c] <= grid[r][c + 1]:
            return

        grid[r][c], grid[r][c + 1] = grid[r][c + 1], grid[r][c]
        swap(East)

    def is_sorted_horizontal(r):
        for c in range(1, size):
            if grid[r][c - 1] > grid[r][c]:
                return False
        return True

    def plant_horizontal(r):
        for c in range(size):
            if get_entity_type() != Entities.Cactus:
                harvest()

                if get_ground_type() != Grounds.Soil:
                    till()

                plant(Entities.Cactus)

            grid[r].append(measure())

            if c > 0:
                swap_prev_horizontal(r, c)

            move(East)

    def sort_horizontal(r):
        move(East)

        while True:
            for c in range(1, size - 1):
                swap_prev_horizontal(r, c)
                swap_next_horizontal(r, c)
                swap_prev_horizontal(r, c)
                if c < size - 2:
                    move(East)

            if is_sorted_horizontal(r):
                move(East)
                move(East)
                break

            for c in range(size - 2, 0, -1):
                swap_next_horizontal(r, c)
                swap_prev_horizontal(r, c)
                swap_next_horizontal(r, c)
                if c > 1:
                    move(West)

            if is_sorted_horizontal(r):
                move(West)
                break

    def swap_prev_vertical(r, c):
        if grid[r - 1][c] <= grid[r][c]:
            return

        grid[r][c], grid[r - 1][c] = grid[r - 1][c], grid[r][c]
        swap(South)

    def swap_next_vertical(r, c):
        if grid[r][c] <= grid[r + 1][c]:
            return

        grid[r][c], grid[r + 1][c] = grid[r + 1][c], grid[r][c]
        swap(North)

    def is_sorted_vertical(c):
        for r in range(1, size):
            if grid[r - 1][c] > grid[r][c]:
                return False
        return True

    def sort_vertical(c):
        move(North)

        while True:
            for r in range(1, size - 1):
                swap_prev_vertical(r, c)
                swap_next_vertical(r, c)
                swap_prev_vertical(r, c)
                if r < size - 2:
                    move(North)

            if is_sorted_vertical(c):
                move(North)
                move(North)
                break

            for r in range(size - 2, 0, -1):
                swap_next_vertical(r, c)
                swap_prev_vertical(r, c)
                swap_next_vertical(r, c)
                if r > 1:
                    move(South)

            if is_sorted_vertical(c):
                move(South)
                break

    for r in range(size):
        grid.append([])
        plant_horizontal(r)
        move(North)

    for r in range(size):
        sort_horizontal(r)
        move(North)

    for c in range(size):
        sort_vertical(c)
        move(East)

    harvest()
