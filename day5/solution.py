from os import path
import math
from typing import List, Set, Optional


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        boarding_passes = input_file.readlines()

        # Your puzzle answer was 959.
        print("Part 1 answer:", max_seat_id(boarding_passes))

        # Your puzzle answer was 527.
        print("Part 2 answer:", my_seat_id(boarding_passes))


def max_seat_id(boarding_passes: List[str]) -> int:
    return max(map(seat_id, boarding_passes))


def row_number(boarding_pass: str) -> int:
    min_row, max_row = 0, 127

    # first 7 letters partition the rows of seats
    # 7th letter handled below
    for partition in boarding_pass[:6]:
        if partition == "F":
            max_row = math.floor((min_row + max_row) / 2)
        else:  # partition == "B"
            min_row = math.ceil((min_row + max_row) / 2)

    # there is probably an elegant way to have this not be a special case :/
    if boarding_pass[6] == "F":
        return min_row
    else:  # partition == "B"
        return max_row


def col_number(boarding_pass: str) -> int:
    min_col, max_col = 0, 7

    # last 3 letters partition the columns
    for partition in boarding_pass[7:]:
        if partition == "L":
            max_col = math.floor((min_col + max_col) / 2)
        else:  # partition == "R"
            min_col = math.ceil((min_col + max_col) / 2)

    # there is probably an elegant way to have this not be a special case :/
    if boarding_pass[9] == "L":
        return min_col
    else:  # partition == "R"
        return max_col


def seat_id(boarding_pass: str) -> int:
    return __seat_id(row_number(boarding_pass), col_number(boarding_pass))


TEST_PASSES = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_row_number():
    assert row_number(TEST_PASSES[0]) == 44
    assert row_number(TEST_PASSES[1]) == 70
    assert row_number(TEST_PASSES[2]) == 14
    assert row_number(TEST_PASSES[3]) == 102


def test_col_number():
    assert col_number(TEST_PASSES[0]) == 5
    assert col_number(TEST_PASSES[1]) == 7
    assert col_number(TEST_PASSES[2]) == 7
    assert col_number(TEST_PASSES[3]) == 4


def test_seat_id():
    assert seat_id(TEST_PASSES[0]) == 357
    assert seat_id(TEST_PASSES[1]) == 567
    assert seat_id(TEST_PASSES[2]) == 119
    assert seat_id(TEST_PASSES[3]) == 820


### PART TWO ###


def __seat_id(row: int, col: int) -> int:
    return row * 8 + col


def my_seat_id(boarding_passes: List[str]) -> Optional[int]:
    existing_ids = existing_seat_ids(boarding_passes)
    missing_seat_ids = all_possible_seat_ids() - existing_ids

    for id in missing_seat_ids:
        if id + 1 in existing_ids and id - 1 in existing_ids:
            return id

    return None


def all_possible_seat_ids() -> Set[int]:
    ids = set()

    for row in range(128):
        for col in range(8):
            ids.add(__seat_id(row, col))

    return ids


def existing_seat_ids(boarding_passes: List[str]) -> Set[int]:
    ids = set()

    for boarding_pass in boarding_passes:
        ids.add(seat_id(boarding_pass))

    return ids


if __name__ == "__main__":
    main()
