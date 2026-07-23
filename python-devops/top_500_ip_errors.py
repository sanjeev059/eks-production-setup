# Which client IP is generating the most HTTP 500 errors?"
# 10.10.1.1 : 3

def client_generating_500_error(new_file):
        top_error = {}
        for line in new_file:
            parts = line.split()
            if parts[3] == "500":
                if parts[0] in top_error:
                    top_error[parts[0]] += 1
                else:
                    top_error[parts[0]] = 1
        print(top_error)




if __name__ == "__main__":
    with open("ip_access.log", 'r') as my_file:
        client_generating_500_error(my_file)