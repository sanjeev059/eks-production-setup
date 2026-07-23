def top_errors(app_file):
    error_count = {}
    latest_error = {}
    largest_val = 0
    for line in app_file:
        part = line.split()
        my_error_code = part[2]
        if  my_error_code in error_count:
            error_count[my_error_code] += 1
        else:
            error_count[my_error_code] = 1
    print(error_count)
    for k,v in error_count.items():
        if v > largest_val:
            largest_val = v
            latest_error[k] = v
            del error_count[k]
    print(latest_error)




if __name__ == "__main__":
    with open("app.log", 'r') as app_file:
        top_errors(app_file)