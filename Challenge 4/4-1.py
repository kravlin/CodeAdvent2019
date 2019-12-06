LOWER_RANGE = 138241
UPPER_RANGE = 674034


def main():
    i = LOWER_RANGE
    possible_passwords = []
    while i <= UPPER_RANGE:
        possible_passwords.append(i)
        i = i + 1
    num_possible_pass = 0
    test_password(167899)
    for password in possible_passwords:
        if test_password(password):
           num_possible_pass = num_possible_pass + 1
    print(f"Num Possiblities: {num_possible_pass}")


def compare_adjacent(num_arr):
    i = 0
    set_of_two = False
    while i < len(num_arr)-1:
        if num_arr[i] == num_arr[i + 1]:
            print(f"comparing num {i} and num {i+1}")
            if i + 2 <= len(num_arr)-1 :
                if(num_arr[i] != num_arr[i + 2]):
                    if i == 0 or (num_arr[i] != num_arr[i - 1]):
                        set_of_two = True
            else:
                if i == 0 or (num_arr[i] != num_arr[i - 1]):                
                    set_of_two = True
        i = i + 1
    return set_of_two


def compare_ascending(num_arr):
    i = 0
    while i < len(num_arr) - 1:
        if num_arr[i] > num_arr[i+1]:
            return False
        i = i + 1
    return True


def test_password(test_pw):
    num_arr = []
    num_arr.append(test_pw // 100000)
    num_arr.append((test_pw % 100000) // 10000)
    num_arr.append((test_pw % 10000) // 1000)
    num_arr.append((test_pw % 1000) // 100)
    num_arr.append((test_pw % 100) // 10)
    num_arr.append(test_pw % 10)
    if compare_ascending(num_arr):
        print(f"Password {test_pw} is ascending")
        if compare_adjacent(num_arr):
            print(f"Password {test_pw} is adjacent")
            return True
    return False


if __name__ == "__main__":
    main()