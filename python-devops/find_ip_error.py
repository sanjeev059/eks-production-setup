def find_errors(ip_errors):
    requsts_dict = {}
    ip = []
    for line in ip_errors:
        part = line.split()
        if part[3] == "500":
            ip  = part[0]
            if ip in requsts_dict:
                requsts_dict[part[0]] += 1
            else:
                requsts_dict[part[0]] = 1
    print(requsts_dict)


if __name__ == "__main__":

    with open("ip_error.log", 'r') as ip_errors:
        find_errors(ip_errors)
