from os import path
from typing import List, Tuple

Instruction = Tuple[str, int]
Program = List[Instruction]


def main() -> None:
    input_path = path.join(path.dirname(__file__), "input.txt")
    with open(input_path) as input_file:
        instructions_str = input_file.read()
        program = to_program(instructions_str)

        # Your puzzle answer was 1553.
        print("Part 1 answer:", debug_program(program))


def debug_program(program: Program) -> int:
    """
    Runs a program that would result in an infinite loop,
    returning the value in the accumulator
    immediately before any instruction is executed a second time.
    """

    accumulator = 0
    address = 0
    seen_addresses = set()

    while True:
        # we've executed the last instruction, apparently
        if address == len(program):
            return accumulator

        # we've been at this address before, which means we're entering an infinite loop
        if address in seen_addresses:
            return accumulator
        else:
            seen_addresses.add(address)

        instruction = program[address]
        op, arg = instruction

        if op == "acc":
            accumulator += arg
            address += 1
        elif op == "jmp":
            address += arg
        else:
            address += 1


def to_program(s: str) -> Program:
    return list(map(to_instruction, s.strip().splitlines()))


def to_instruction(s: str) -> Instruction:
    op, arg = s.split(" ")
    return (op, int(arg))


def test_part_1():
    program = to_program(
        """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
    )

    assert debug_program(program) == 5


if __name__ == "__main__":
    main()
