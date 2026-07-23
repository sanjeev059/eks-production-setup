
# Which URL Generated the Most HTTP 500 Errors?
def url_generated_most_http_errors(aap_log):
    url_status = {}
    largest_url = ""
    largest_count = 0
    for line in aap_log:
        part = line.split()
        #url is my key
        url = part[2]
        status_code = part[3]
        if status_code == "500":
            if url in url_status:
                url_status[url] += 1
            else:
                url_status[url] = 1
    print(url_status)
    for key, value in url_status.items():
        if value > largest_count:
            largest_count = value
            largest_url = key
    print(f"{largest_url}:{largest_count}")



if __name__ == "__main__":

    with open("url.log", "r") as logger_file:
        # most_request_made_by_ip(logger_file)
        url_generated_most_http_errors(logger_file)