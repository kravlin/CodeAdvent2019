def calculate_fuel(mass):
	div_result = mass//3
	sub_result = div_result - 2
	if sub_result < 0:
		return 0
	return sub_result


def main():
	f = open("1-1-input.txt", "r")
	total_fuel = 0
	for line in f:
		needed_fuel = calculate_fuel(int(line))
		total_fuel = total_fuel + needed_fuel
		while(needed_fuel != 0):
			needed_fuel = calculate_fuel(needed_fuel)
			total_fuel = total_fuel + needed_fuel
	print(f"Total Fuel: {total_fuel}")


if __name__ == "__main__":
	main()