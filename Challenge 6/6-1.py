INPUT_FILE = "puzzle_input.txt"


def load_file(location):
    file = open(location, 'r')
    orbits = []
    for line in file:
        host, client = line.split(")")
        orbits.append((host, client))
    return orbits


def main():
    orbits = load_file(INPUT_FILE)
    print(orbits)


if __name__ == "__main__":
    main()
