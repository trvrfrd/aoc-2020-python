from os import path
from typing import List, Dict


REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        file_data = input_file.read()
        # Your puzzle answer was 213.
        print("Part 1 answer:", count_valid_passports(file_data))


def count_valid_passports(batch_file: str) -> int:
    passport_data = batch_file.strip().split("\n\n")
    count = 0

    for datum in passport_data:
        if is_valid_passport(datum):
            count += 1

    return count


def is_valid_passport(passport_datum: str, required_fields=REQUIRED_FIELDS) -> bool:
    for field in required_fields:
        if f"{field}:" not in passport_datum:
            return False

    return True


def test_part_1():
    data = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()

    assert count_valid_passports(data) == 2


if __name__ == "__main__":
    main()
