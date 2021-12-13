import time
# import your file here
import subprocess
import random

def test_mean_time(number_of_tests, bat_file, text_to_encode=['"secret message?"','"secret message?11"']):
    times = []
    for i in range(number_of_tests):
        with open(bat_file, "w") as dft:
            dft.truncate()
            # cd to location of your algorithm
            dft.write("cd DFT\n")
            # write a command to run your program with {text_to_encode} to attach custom message to encode
            if isinstance(text_to_encode, str):
                dft.write(f"python test.py -o test2.jpg -t {text_to_encode} -a 30 -v test.jpg")
            else:
                dft.write(f"python test.py -o test2.jpg -t {text_to_encode[random.randint(0,len(text_to_encode)-1)]} -a 30 -v test.jpg")
        start = time.time()
        subprocess.call([r'dft.bat'])
        end = time.time()
        times.append(end - start)
    return times


def count_mean_time(times):
    sum = 0
    for i in times:
        sum += i
    return sum / len(times)


if __name__ == "__main__":
    # how many times you want to test, bat file name
    times = test_mean_time(100, bat_file="dft.bat")
    print(count_mean_time(times))
