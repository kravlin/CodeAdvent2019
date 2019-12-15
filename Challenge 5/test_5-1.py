
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
    if(computer.output_opcode() == 10):
        assert True
    else:
        assert False
