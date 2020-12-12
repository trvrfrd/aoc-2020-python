from os import path
import re
from typing import List


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        rules = input_file.read().strip()

        # Your puzzle answer was 378.
        print("Part 1 answer:", count_possible_shiny_gold_holders(rules))


def count_possible_shiny_gold_holders(rules: str) -> int:
    count = 0
    # o lawd this will be a mess
    patterns = [r"^(\w+ \w+) bags contain.+(\d) shiny gold.+$"]
    # we don't want to double-count bags that can be contained by more than one kind of bag
    bags_seen = set(["shiny gold"])

    for pattern in patterns:
        # each bag we match can contain a bag of interest, so:
        for match in re.finditer(pattern, rules, re.MULTILINE):
            # get the description of the bag out of the match
            containing_bag_descriptor = match[1]
            # if we haven't already counted this bag as able to contain a bag of interest:
            if containing_bag_descriptor not in bags_seen:
                count += 1
                bags_seen.add(containing_bag_descriptor)
                # add a search for bags that can, in turn, contain this bag
                containing_bag_pattern = (
                    fr"^(\w+ \w+) bags contain.+(\d) {containing_bag_descriptor}.+$"
                )
                patterns.append(containing_bag_pattern)

    return count


def test_part_1():
    rules = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip()
    assert count_possible_shiny_gold_holders(rules) == 4


if __name__ == "__main__":
    main()
