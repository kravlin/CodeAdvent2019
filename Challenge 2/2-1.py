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
	opcodes[1] = 12
	opcodes[2] = 2
	output = run_program(opcodes)
	print(f"Opcode at 0: {output}")


if __name__ == "__main__":
	main()