
from intcode import Intcode


def test_add_opcode_position():
    computer = Intcode([1, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 25:
        assert True
    else:
        assert False


def test_add_opcode_immediate():
    computer = Intcode([1101, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 11:
        assert True
    else:
        assert False


def test_add_opcode_mixed_1():
    computer = Intcode([1001, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 16:
        assert True
    else:
        assert False


def test_add_opcode_mixed_2():
    computer = Intcode([101, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 20:
        assert True
    else:
        print(computer.program[0])
        assert False


def test_mul_opcode_position():
    computer = Intcode([2, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 150:
        assert True
    else:
        assert False


def test_mul_opcode_immediate():
    computer = Intcode([1102, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 30:
        assert True
    else:
        assert False


def test_mul_opcode_mixed_1():
    computer = Intcode([1002, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 60:
        assert True
    else:
        print(computer.program[0])
        assert False


def test_mul_opcode_mixed_2():
    computer = Intcode([102, 5, 6, 0, 99, 10, 15], None)
    computer.run_program()
    if computer.program[0] == 75:
        assert True
    else:
        print(computer.program[0])
        assert False


def test_output_opcode():
    computer = Intcode([4, 2, 10, 99], None)
    if(computer.output_opcode(0) == 10):
        assert True
    else:
        assert False


def test_output_opcode_immediate():
    computer = Intcode([104, 2, 99], None)
    output = computer.output_opcode(1)
    print(output)
    if(output == 2):
        assert True
    else:
        assert False


def test_jump_true_opcode():
    computer = Intcode([5, 1, 4, 99, 44], None)
    computer.jump_true_opcode(0, 0)
    if computer.pointer == 44:
        assert True
    else:
        assert False


def test_jump_true_opcode_immediate():
    computer = Intcode([105, 1, 4, 99, 44], None)
    computer.jump_true_opcode(1, 1)
    if computer.pointer == 4:
        assert True
    else:
        assert False


def test_jump_true_opcode_mixed_1():
    computer = Intcode([5, 1, 4, 99, 44], None)
    computer.jump_true_opcode(1, 0)
    if computer.pointer == 44:
        assert True
    else:
        assert False


def test_jump_true_opcode_mixed_2():
    computer = Intcode([5, 1, 4, 99, 44], None)
    computer.jump_true_opcode(0, 1)
    if computer.pointer == 4:
        assert True
    else:
        assert False


def test_jump_true_fail():
    computer = Intcode([5, 2, 0, 99], None)
    computer.jump_true_opcode(0, 0)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_true_fail_immediate():
    computer = Intcode([5, 0, 33, 99], None)
    computer.jump_true_opcode(1, 1)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_true_fail_mixed_1():
    computer = Intcode([5, 0, 0, 99], None)
    computer.jump_true_opcode(1, 0)
    print(computer.pointer)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_true_fail_mixed_2():
    computer = Intcode([5, 2, 0, 99], None)
    computer.jump_true_opcode(0, 1)
    print(computer.pointer)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_false_opcode():
    computer = Intcode([6, 4, 4, 99, 0], None)
    computer.jump_false_opcode(0, 0)
    if computer.pointer == 0:
        assert True
    else:
        assert False


def test_jump_false_opcode_immediate():
    computer = Intcode([6, 0, 4, 99, 44], None)
    computer.jump_false_opcode(1, 1)
    if computer.pointer == 4:
        assert True
    else:
        assert False


def test_jump_false_opcode_mixed_1():
    computer = Intcode([6, 0, 4, 99, 44], None)
    computer.jump_false_opcode(1, 0)
    if computer.pointer == 44:
        assert True
    else:
        assert False


def test_jump_false_opcode_mixed_2():
    computer = Intcode([6, 4, 1, 99, 0], None)
    computer.jump_false_opcode(0, 1)
    if computer.pointer == 1:
        assert True
    else:
        assert False


def test_jump_false_fail():
    computer = Intcode([6, 2, 1, 99], None)
    computer.jump_false_opcode(0, 0)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_false_fail_immediate():
    computer = Intcode([6, 2, 33, 99], None)
    computer.jump_false_opcode(1, 1)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_false_fail_mixed_1():
    computer = Intcode([6, 2, 0, 99], None)
    computer.jump_false_opcode(1, 0)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_jump_false_fail_mixed_2():
    computer = Intcode([6, 2, 32, 99], None)
    computer.jump_false_opcode(0, 1)
    if computer.pointer == 3:
        assert True
    else:
        assert False


def test_less_than_succeed():
    computer = Intcode([7, 1, 2, 0, 99], None)
    computer.less_than_opcode(0, 0)
    if computer.program[0] == 1:
        assert True
    else:
        assert False


def test_less_than_fail():
    computer = Intcode([7, 5, 6, 0, 99, 31, 29], None)
    computer.less_than_opcode(0, 0)
    if computer.program[0] == 0:
        assert True
    else:
        assert False


def test_equal_succeed():
    computer = Intcode([8, 2, 2, 0, 99], None)
    computer.equals_opcode(0, 0)
    if computer.program[0] == 1:
        assert True
    else:
        assert False


def test_equal_fail():
    computer = Intcode([8, 5, 6, 0, 99, 31, 29], None)
    computer.equals_opcode(0, 0)
    if computer.program[0] == 0:
        assert True
    else:
        assert False
