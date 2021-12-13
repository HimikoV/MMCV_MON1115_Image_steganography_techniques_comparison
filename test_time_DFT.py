import time
# import your file here
import DFT.test as dft


def test_mean_time(number_of_tests, text_to_encode="secret message?"):
    for i in range(number_of_tests):
        times = []
        start = time.time()
        # run the algorithm
        # use text_to_encode as your testing message, you can use it as array of different messages
        # using i as your enumerator of the list
        end = time.time()
        times.append(start - end)
    return times


def count_mean_time(times):
    sum = 0
    for i in times:
        sum += i
    return sum / len(times)


if __name__ == "__main__":
    times = test_mean_time(100)
    print(count_mean_time(times))
