from os import path
from typing import List


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as infile:
        password_database = infile.readlines()
        # Your puzzle answer was 546.
        print(
            "Part 1 answer:", count_valid_passwords(password_database, policy="total")
        )
        # Your puzzle answer was 275.
        print(
            "Part 2 answer:",
            count_valid_passwords(password_database, policy="positions"),
        )


### PART 1 ###


def count_valid_passwords(password_database: List[str], policy: str) -> int:
    return len(
        list(filter(lambda p: is_valid_password(p, policy=policy), password_database))
    )


def is_valid_password(parameters_and_password: str, policy: str) -> bool:
    parameters, password = parameters_and_password.split(": ")
    num_params, required_letter = parameters.split(" ")
    num1, num2 = map(int, num_params.split("-"))

    if policy == "total":
        min_count, max_count = num1, num2
        return min_count <= password.count(required_letter) <= max_count
    elif policy == "positions":
        pos1, pos2 = num1, num2  # 1-indexed positions in the password str
        # logical xor: exactly one of the chars should match
        return (password[pos1 - 1] == required_letter) ^ (
            password[pos2 - 1] == required_letter
        )  # wow i really hate what black did here, oh well!!!
    else:
        raise Exception  # whatever


def test_part_1():
    example = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert count_valid_passwords(example, policy="total") == 2


### PART 2 ###


def test_part_2():
    example = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert count_valid_passwords(example, policy="positions") == 1


if __name__ == "__main__":
    main()
