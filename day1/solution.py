from os import path
from itertools import combinations
from typing import List, Tuple


def main() -> None:
    dirname = path.dirname(__file__)
    input_path = path.join(dirname, "input.txt")

    with open(input_path) as infile:
        entries = list(map(int, infile.readlines()))

        # Your puzzle answer was 1016131.
        print("Part 1 answer:", multipy_two_entries_that_sum_to_n(entries, 2020))

        # Your puzzle answer was 276432018.
        print("Part 2 answer:", multipy_three_entries_that_sum_to_n(entries, 2020))


### PART 1 ###


def entries_that_sum_to_n(
    entries: List[int], k_combinations: int, n: int
) -> Tuple[int, ...]:
    for combo in combinations(entries, k_combinations):
        if sum(combo) == n:
            return combo

    return ()


def multipy_two_entries_that_sum_to_n(entries: List[int], n: int) -> int:
    nums = entries_that_sum_to_n(entries, 2, n)
    return nums[0] * nums[1]


def test_part_1():
    entries = [1721, 979, 366, 299, 675, 1456]
    n = 2020
    assert multipy_two_entries_that_sum_to_n(entries, n) == 514579


### PART 2 ###


def multipy_three_entries_that_sum_to_n(entries: List[int], n: int) -> int:
    nums = entries_that_sum_to_n(entries, 3, n)
    return nums[0] * nums[1] * nums[2]


def test_part_2():
    entries = [1721, 979, 366, 299, 675, 1456]
    n = 2020
    assert multipy_three_entries_that_sum_to_n(entries, n) == 241861950


if __name__ == "__main__":
    main()
