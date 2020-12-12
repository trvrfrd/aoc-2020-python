from os import path
import re
from typing import List, Dict


REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        file_data = input_file.read().strip()

        # Your puzzle answer was 213.
        print("Part 1 answer:", count_valid_passports(file_data))

        # Your puzzle answer was 147.
        print("Part 2 answer:", count_valid_passports(file_data, strict=True))


def count_valid_passports(batch_file: str, strict=False) -> int:
    passport_data = batch_file.strip().split("\n\n")
    count = 0

    for datum in passport_data:
        if is_valid_passport(datum, strict=strict):
            count += 1

    return count


def is_valid_passport(
    passport_datum: str, required_fields=REQUIRED_FIELDS, strict=False
) -> bool:
    for field in required_fields:
        if f"{field}:" not in passport_datum:
            return False

    if strict:
        passport_datum = passport_datum.replace("\n", " ")
        kv_pair_strs = passport_datum.split(" ")
        for pair_str in kv_pair_strs:
            field, value = pair_str.split(":")
            if not is_valid_value(field, value):
                return False

    return True


def is_valid_value(field: str, value: str) -> bool:
    if field == "byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002
    if field == "iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020
    if field == "eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030
    if field == "hgt":
        num_match = re.match(r"\d+", value)
        if num_match:
            magnitude = int(num_match[0])
        if value.endswith("cm"):
            return 150 <= magnitude <= 193
        elif value.endswith("in"):
            return 59 <= magnitude <= 76
        else:
            return False
    if field == "hcl":
        # a # followed by exactly six characters 0-9 or a-f
        return re.match(r"^#[0-9a-f]{6}$", value) is not None
    if field == "ecl":
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if field == "pid":
        # a nine-digit number, including leading zeroes
        return re.match(r"^[0-9]{9}$", value) is not None
    if field == "cid":
        return True

    return False


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


def test_part_2_invalid():
    data = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".strip()

    assert count_valid_passports(data, strict=True) == 0


def test_part_2_valid():
    data = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip()

    assert count_valid_passports(data, strict=True) == 4


if __name__ == "__main__":
    main()
