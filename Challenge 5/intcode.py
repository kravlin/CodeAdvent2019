import logging
import argparse


class Intcode():
    program = []
    logger = None
    pointer = 0

    def __init__(self, program, verbosity):
        self.program = program
        self.setup_logging(verbosity)

    def setup_logging(self, verbosity):
        if verbosity is None:
            logging.basicConfig(level=logging.ERROR)
        elif verbosity == 0:
            logging.basicConfig(level=logging.WARNING)
        elif verbosity == 1:
            logging.basicConfig(level=logging.INFO)
        elif verbosity > 1:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.ERROR)
        self.logger = logging.getLogger()

    def store(self, store_loc, store_val):
        self.logger.info(f"Storing {store_val} at {store_loc}")
        self.program[store_loc] = store_val

    def add_opcode(self, mode1, mode2):
        self.logger.info(f"Addition Opcode at {self.pointer}")
        first_op = self.get_value(mode1, self.pointer + 1)
        second_op = self.get_value(mode2, self.pointer + 2)
        store_loc = self.get_value(1, self.pointer + 3)
        self.logger.debug(f"Adding {self.pointer} and {self.pointer}")
        store_val = first_op + second_op
        self.store(store_loc, store_val)
        self.pointer += 4

    def multi_opcode(self, mode1, mode2):
        self.logger.info(f"Multiplcation Opcode at {self.pointer}")
        first_op = self.get_value(mode1, self.pointer + 1)
        second_op = self.get_value(mode2, self.pointer + 2)
        store_loc = self.get_value(1, self.pointer + 3)
        self.logger.debug(f"Multiplying {first_op} and {second_op}")
        store_val = first_op * second_op
        self.store(store_loc, store_val)
        self.pointer += 4

    def input_opcode(self):
        self.logger.info(f"Input Opcode at {self.pointer}")
        store_loc = self.get_value(1, self.pointer + 1)
        store_val = int(input("Please input a #: "))
        self.store(store_loc, store_val)
        self.pointer += 2

    def output_opcode(self, mode1):
        self.logger.info(f"Output Opcode at {self.pointer}")
        return_value = self.get_value(mode1, self.pointer + 1)
        self.pointer += 2
        return return_value

    def jump_true_opcode(self, mode1, mode2):
        self.logger.info(f"Jump if True Opcode at {self.pointer}")
        bool_val = self.get_value(mode1, self.pointer + 1)
        jump_val = self.get_value(mode2, self.pointer + 2)
        if bool_val != 0:
            self.logger.debug(f"Jumping to {jump_val}")
            self.pointer = jump_val
        else:
            self.logger.debug("Value was false. Not Jumping")
            self.pointer += 3

    def jump_false_opcode(self, mode1, mode2):
        self.logger.debug(f"Jump if False Opcode at {self.pointer}")
        bool_val = self.get_value(mode1, self.pointer + 1)
        jump_val = self.get_value(mode2, self.pointer + 2)
        if bool_val == 0:
            self.logger.debug(f"Jumping to {jump_val}")
            self.pointer = jump_val
        else:
            self.logger.debug("Value was true. Not Jumping")
            self.pointer += 3

    def less_than_opcode(self, mode1, mode2):
        first_val = self.get_value(mode1, self.pointer + 1)
        second_val = self.get_value(mode2, self.pointer + 2)
        store_loc = self.get_value(1, self.pointer + 3)
        if first_val < second_val:
            self.store(store_loc, 1)
        else:
            self.store(store_loc, 0)
        self.pointer += 4

    def equals_opcode(self, mode1, mode2):
        first_val = self.get_value(mode1, self.pointer + 1)
        second_val = self.get_value(mode2, self.pointer + 2)
        store_loc = self.get_value(1, self.pointer + 3)
        if first_val == second_val:
            self.store(store_loc, 1)
        else:
            self.store(store_loc, 0)
        self.pointer += 4

    def run_program(self, ending=None):
        if ending is None:
            ending = 99999999
        else:
            ending = ending[0]
        while self.pointer != 99 and self.pointer < ending:
            self.logger.debug(f"Pointer is at {self.pointer}")
            opcode, mode1, mode2, mode3 = self.parse_opcode()
            self.logger.debug(f"Opcode: {opcode}, mode 1: {mode1}, mode 2: {mode2}")
            if opcode == 1:  # Add
                self.add_opcode(mode1, mode2)
            elif opcode == 2:  # Multiply
                self.multi_opcode(mode1, mode2)
            elif opcode == 3:  # Input
                self.input_opcode()
            elif opcode == 4:  # Output
                print(f"Outputting Value: {self.output_opcode(mode1)}")
            elif opcode == 5:  # Jump if TRUE
                self.jump_true_opcode(mode1, mode2)
            elif opcode == 6:  # Jump if FALSE
                self.jump_false_opcode(mode1, mode2)
            elif opcode == 7:  # Less Than
                self.less_than_opcode(mode1, mode2)
            elif opcode == 8:  # Equals
                self.equals_opcode(mode1, mode2)
            elif opcode == 99:
                self.logger.debug("Ending Program")
                return True
            else:
                print(f"System Panic!! Opcode was {opcode}")
                return False
        return False

    def get_value(self, mode, opcode_loc):
        if mode == 0:
            self.logger.info(f"Pulling using position (mode 0) at {opcode_loc}")
            self.logger.debug(f"Location is {self.program[opcode_loc]}")
            return_val = self.program[self.program[opcode_loc]]
            self.logger.info(f"Returning {return_val}")
            return return_val
        elif mode == 1:
            self.logger.info(f"Pulling using immediate (mode 1) at {opcode_loc}")
            self.logger.info(f"Returning {self.program[opcode_loc]}")
            return self.program[opcode_loc]
        else:
            print(f"Unknown mode {mode}")
            return False

    # Parses the opcode value so we're able[to actually te]l what's going on
    def parse_opcode(self):
        opcode_val = self.program[self.pointer]
        opcode = int(opcode_val % 100)
        mode_1 = int((opcode_val % 1000) // 100)
        mode_2 = int((opcode_val % 10000) // 1000)
        mode_3 = int((opcode_val % 100000) // 10000)
        return (opcode, mode_1, mode_2, mode_3)


def main(verbosity, ending):
    f = open("puzzle_input.txt", "r")
    loaded_program = f.readline().split(",")
    # Convert what was read in into ints
    print(f"Program Loaded Successfully")
    i = 0
    print(f"Converting program to ints")
    while i < len(loaded_program):
        loaded_program[i] = int(loaded_program[i])
        i = i + 1
    computer = Intcode(loaded_program, verbosity)
    print(f"Running Program")
    output = computer.run_program(ending)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--verbosity",
                        help="increase output verbosity",
                        action="count")
    parser.add_argument("-e",
                        "--ending",
                        help="instruction to end the code on",
                        type=int,
                        nargs=1)
    args = parser.parse_args()
    main(args.verbosity, args.ending)
