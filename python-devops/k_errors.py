# roblem 8 - Print the Last K ERROR Logs

def last_k_errors(app_log,k):
    error_dict = []
    for line in app_log:
        parts = line.split()
        if parts[2] == "ERROR":
            error_dict.append(line)
    print(f"{error_dict}")

    print(error_dict[-2:])

if __name__ == "__main__":
    with open("application.log", 'r') as app_log:
        k = 3
        last_k_errors(app_log,k)