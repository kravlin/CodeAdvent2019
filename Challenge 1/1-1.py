def calcuate_fuel(mass):
	div_result = mass//3
	sub_result = div_result - 2
	return sub_result


def main():
	f = open("1-1-input.txt", "r")
	total_fuel = 0
	for line in f:
		total_fuel = total_fuel + calcuate_fuel(int(line))
	print(f"Total Fuel: {total_fuel}")


if __name__ == "__main__":
	main()