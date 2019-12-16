import logging


class Intcode():

    program = []
    position = 0
    logger = logging.getLogger()

    def __init__(self, program):
        self.program = program

    def parse_opcode():
        pass

    def run_program():
        pass

    def opcode_add():
        pass

    def opcode_mul():
        pass

    def opcode_in():
        pass

    def opcode_out():
        pass

    def opcode_jump_true():
        pass

    def opcode_jump_false():
        pass

    def opcode_less_than():
        pass

    def opcode_equals():
        pass

def run_program(opcodes):
    cur_opcode = 0
    while int(opcodes[cur_opcode]) != 99:
        if int(opcodes[cur_opcode]) == 1:
            f_num_loc = int(opcodes[cur_opcode + 1])
            s_num_loc = int(opcodes[cur_opcode + 2])
            store_loc = int(opcodes[cur_opcode + 3])
            sum = int(opcodes[f_num_loc]) + int(opcodes[s_num_loc])
            opcodes[store_loc] = sum
        elif int(opcodes[cur_opcode]) == 2:
            f_num_loc = int(opcodes[cur_opcode + 1])
            s_num_loc = int(opcodes[cur_opcode + 2])
            store_loc = int(opcodes[cur_opcode + 3])
            sum = int(opcodes[f_num_loc]) * int(opcodes[s_num_loc])
            opcodes[store_loc] = sum
        else:
            err_opcode = opcodes[cur_opcode]
            print(f"WTF. Error will robinson! Opcode was {err_opcode}")
        cur_opcode = cur_opcode + 4
    return opcodes[0]


def main():
    f = open("puzzle_input.txt", "r")
    opcodes = f.readline().split(",")
    len_opcodes = len(opcodes)
    num_opcodes = len_opcodes//4
    print(f"{len_opcodes} instructions added")
    print(f"{num_opcodes} instructions provided")
    output = 0
    noun = 0
    verb = 0
    while output != 19690720:
        testcodes = opcodes[:]
        testcodes[1] = noun
        testcodes[2] = verb
        output = run_program(testcodes)
        if output != 19690720:
            if noun < 99:
                noun = noun + 1
            else:
                noun = 0
                verb = verb + 1
    out_values = 100 * noun + verb
    print(out_values)


if __name__ == "__main__":
    main()