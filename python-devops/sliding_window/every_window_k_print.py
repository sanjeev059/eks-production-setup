def sliding_window(numbers, k):

    for i in range((len(numbers) - k) + 1):

        print(numbers[i:i+k])
if __name__ == "__main__":

    numbers = [2, 3, 5, 2, 9, 7, 1]
    k = 3

    sliding_window(numbers, k)