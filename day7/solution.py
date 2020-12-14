from os import path
import re
from typing import List


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        rules = input_file.read().strip()

        # Your puzzle answer was 378.
        print("Part 1 answer:", count_possible_shiny_gold_holders(rules))

        # Your puzzle answer was 27526.
        print("Part 2 answer:", count_bags_inside_bag("shiny gold", rules))


def count_possible_shiny_gold_holders(rules: str) -> int:
    count = 0
    # o lawd this will be a mess
    patterns = [r"^(\w+ \w+) bags contain.+(\d) shiny gold.+$"]
    # we don't want to double-process bags that can be contained by more than one kind of bag
    bags_seen = set(["shiny gold"])

    for pattern in patterns:
        # each bag we match can contain a bag of interest, so:
        for match in re.finditer(pattern, rules, re.MULTILINE):
            # get the description of the containing bag out of the match
            outer_bag_description = match[1]
            # if we haven't already counted this bag as able to contain a bag of interest:
            if outer_bag_description not in bags_seen:
                count += 1
                bags_seen.add(outer_bag_description)
                # add a search for bags that can, in turn, contain this bag
                containing_bag_pattern = (
                    fr"^(\w+ \w+) bags contain.+(\d) {outer_bag_description}.+$"
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


### PART TWO ###


def count_bags_inside_bag(bag_description: str, rules: str) -> int:
    # we don't want to count the bag itself, just all bags within it
    return count_required_bags(bag_description, rules) - 1


def count_required_bags(bag_description: str, rules: str) -> int:
    # hope we don't have any circular dependencies lol
    pattern = rf"^{bag_description} bags contain.+$"

    match = re.search(pattern, rules, re.MULTILINE)

    if match:
        rule = match[0]

        if rule.endswith("no other bags."):
            return 1

        count = 1
        inner_bag_pattern = r"(\d) (\w+ \w+) bags?"

        for inner_bag_match in re.finditer(inner_bag_pattern, rule):
            inner_bag_count = int(inner_bag_match[1])
            inner_bag_description = inner_bag_match[2]

            count += inner_bag_count * count_required_bags(inner_bag_description, rules)

        return count
    else:
        raise Exception  # whatever


def test_part_2():
    rules = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip()

    assert count_bags_inside_bag("shiny gold", rules) == 126


if __name__ == "__main__":
    main()
