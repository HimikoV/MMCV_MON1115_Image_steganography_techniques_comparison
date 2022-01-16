import time
# import your file here
import subprocess
import random


def bat_overrite(bat_file, text_to_encode=['"secret message?"', '"secret message?11"']):
    with open(bat_file, "w") as dft:
        dft.truncate()
        # cd to location of your algorithm
        dft.write("cd DFT\n")
        # write a command to run your program with {text_to_encode} to attach custom message to encode
        if isinstance(text_to_encode, str):
            dft.write(f"python test.py -o test2.jpg -t {text_to_encode} -a 30 -v test.jpg")
        else:
            dft.write(
                f"python test.py -o test2.jpg -t {text_to_encode[random.randint(0, len(text_to_encode) - 1)]} -a 30 -v test.jpg")
    return


def gather_mean_time(number_of_tests):
    times = []
    for i in range(number_of_tests):
        bat_overrite(bat_file="dft.bat")
        start = time.time()
        subprocess.call([r'dft.bat'])
        end = time.time()
        times.append(end - start)
    return times


def count_max_charr_length(incremented_string='"x"'):
    for i in range(100):
        incremented_string = incremented_string[:-1]
        incremented_string += 'x"'
        bat_overrite(bat_file="dft.bat", text_to_encode=incremented_string)
        subprocess.call([r'dft.bat'])
        if subprocess.run([r'dft.bat']).returncode == 1:
            return len(incremented_string) - 1
    return len(incremented_string)


def count_mean_time(times):
    sum = 0
    for i in times:
        sum += i
    return sum / len(times)


if __name__ == "__main__":
    # how many times you want to test, bat file name

    max_length = count_max_charr_length()
    times = gather_mean_time(100)
    print(f"mean time: {count_mean_time(times)}")
    print(f"max length in charr of encoded message {max_length}")
