import re


def main():
    needed_time = False
    counter = 0
    file = open("access_log_Jul95")

    for line in file:
        if re.search(r"01/Jul/1995:00:30", line):
            needed_time = False
            break
        if re.search(r"01/Jul/1995:00:20", line):
            needed_time = True
        if needed_time and re.search(r"NASA", line):
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
