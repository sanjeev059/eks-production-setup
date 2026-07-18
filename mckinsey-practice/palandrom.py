
if __name__ == '__main__':
    pal_str = input(str())
    rev_str = ""
    #
    # print(pal_str[-3])

    for i in range(len(pal_str) - 1 , -1, -1):
        print(pal_str[i])
        rev_str = rev_str + pal_str[i]

    if rev_str == pal_str:
        print("its pal")
    else:
        print("not a pal")


