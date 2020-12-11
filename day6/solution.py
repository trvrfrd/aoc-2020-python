from os import path
from typing import List


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")

    with open(input_path) as input_file:
        answer_groups = input_file.read().strip().split("\n\n")

        # Your puzzle answer was 6930.
        print("Part 1 answer:", count_questions_anyone_answered(answer_groups))

        # Your puzzle answer was 3585.
        print("Part 2 answer:", count_questions_everyone_answered(answer_groups))


def count_questions_anyone_answered(answer_groups: List[str]) -> int:
    count = 0

    for answer_group in answer_groups:
        answer_group = answer_group.replace("\n", "")
        count += len(set(answer_group))

    return count


### PART TWO ###


# this could probably all be one reduce call but I don't love functional Python so far
def count_questions_everyone_answered(answer_groups: List[str]) -> int:
    count = 0

    for answer_group in answer_groups:
        # start with the set of all answers in that group
        # we will reduce it via intersection in the next step
        answers_intersection = set(answer_group.replace("\n", ""))

        for answer in answer_group.split("\n"):
            answers_intersection = answers_intersection & set(answer)

        count += len(answers_intersection)

    return count


if __name__ == "__main__":
    main()
