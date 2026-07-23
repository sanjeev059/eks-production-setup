def top_k_ip(ip_log, k):
    k_dict = {}

    for line in ip_log:
        parts = line.split()
        ip = parts[0]
        if parts[3] == "500":
            if ip in k_dict:
                k_dict[ip] += 1
            else:
                k_dict[ip] = 1

    for i in range(k):
        largest = 0
        largest_ip_key = ""
        for key, v in k_dict.items():
            if v > largest:
                largest = v
                largest_ip_key = key
        print(f"{largest}:{largest_ip_key}")
        del k_dict[largest_ip_key]

if __name__ == "__main__":
    with open("ip.log", 'r') as ip_log:
        k = 3
        top_k_ip(ip_log,k)