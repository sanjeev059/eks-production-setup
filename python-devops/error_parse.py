def find_error_log(new_file):
    error_line = []
    line_number = 0
    for line in new_file:
        line_number += 1
        my_error_key = line.split()
        if my_error_key[2] == "ERROR":
            print(f"Line {line_number}: {line.strip()}")


if __name__ == "__main__":

    with open("error.log", 'r') as error_file:
        find_error_log(error_file)