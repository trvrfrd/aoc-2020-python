from os import path
from typing import List, Tuple

Slope = Tuple[int, int]


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        tree_map = list(map(str.strip, input_file.readlines()))  # freakin' newlines

        # Your puzzle answer was 234.
        print("Part 1 answer:", count_tree_collisions(tree_map, slope=(3, 1)))

        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]

        # Your puzzle answer was 5813773056.
        print("Part 2 answer:", check_slopes_and_multiply(tree_map, slopes))


def count_tree_collisions(tree_map: List[str], slope: Slope) -> int:
    width = len(tree_map[0])
    height = len(tree_map)
    x = 0
    y = 0
    delta_x, delta_y = slope
    count = 0

    while y < height:
        x = (x + delta_x) % width  # map repeats horizontally
        y += delta_y  # but not vertically; when we reach the end, we're done

        if y >= height:
            break

        if tree_map[y][x] == "#":
            count += 1

    return count


def test_part_1():
    example_map = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert count_tree_collisions(example_map, slope=(3, 1)) == 7


### PART TWO ###


def check_slopes_and_multiply(tree_map: List[str], slopes: List[Slope]) -> int:
    product = 1

    for slope in slopes:
        product *= count_tree_collisions(tree_map, slope)

    return product


def test_part_2():
    example_map = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    assert check_slopes_and_multiply(example_map, slopes) == 336


if __name__ == "__main__":
    main()
