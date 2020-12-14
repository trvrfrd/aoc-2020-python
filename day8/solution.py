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
        print("Part 1 answer:", run_program(program)[1])

        debugged_program = debug_program(program)

        # Your puzzle answer was 1877.
        print("Part 2 answer:", run_program(debugged_program)[1])


def run_program(program: Program) -> Tuple[bool, int]:
    """
    Runs a program that could result in an infinite loop,
    returning a tuple consisting of:
    - a bool indicating whether the program ran to completion
    - the int in the accumulator when the program terminated (or began an infinite loop)
    """

    accumulator = 0
    address = 0
    seen_addresses = set()

    while address < len(program):
        if address in seen_addresses:
            # we've been at this address before, which means we're entering an infinite loop
            return (False, accumulator)

        seen_addresses.add(address)

        instruction = program[address]
        op, arg = instruction

        if op == "acc":
            accumulator += arg
            address += 1
        elif op == "jmp":
            address += arg
        else:  # nop
            address += 1

    # we've executed the last instruction, apparently
    return (True, accumulator)


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

    assert run_program(program) == (False, 5)


### PART TWO ###


def debug_program(program: Program) -> Program:
    """
    Takes a program with a known infinite loop bug
    and changes one instruction at a time until the program terminates normally,
    returning the working program.
    """

    for address in range(len(program)):
        instruction = program[address]
        op, arg = instruction

        if op == "nop":
            new_op = "jmp"
        elif op == "jmp":
            new_op = "nop"
        else:
            continue

        new_program = program.copy()
        new_program[address] = (new_op, arg)

        output = run_program(new_program)

        if output[0]:
            break

    return new_program


def test_part_2():
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
    debugged_program = debug_program(program)
    assert run_program(debugged_program) == (True, 8)


if __name__ == "__main__":
    main()
